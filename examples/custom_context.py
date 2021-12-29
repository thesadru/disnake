import random

import disnake
from disnake.ext import commands


class MyContext(commands.Context):
    async def tick(self, value):
        # reacts to the message with an emoji
        # depending on whether value is True or False
        # if its True, it'll add a green check mark
        # otherwise, it'll add a red cross mark
        emoji = "\N{WHITE HEAVY CHECK MARK}" if value else "\N{CROSS MARK}"
        try:
            # this will react to the command author's message
            await self.message.add_reaction(emoji)
        except disnake.HTTPException:
            # sometimes errors occur during this, for example
            # maybe yo don't have permission to do that
            # we don't mind, so we can just ignore them
            pass


class MyBot(commands.Bot):
    async def get_context(self, message, *, cls=MyContext):
        # when yo override this method, yo pass yor new Context
        # subclass to the super() method, which tells the bot to
        # use the new MyContext class
        return await super().get_context(message, cls=cls)


bot = MyBot(command_prefix="!")


@bot.command()
async def guess(ctx, number: int):
    """Guess a random number from 1 to 6."""
    # explained in a previos example, this gives yo
    # a random number from 1-6
    value = random.randint(1, 6)
    # with yor new helper function, yo can add a
    # green check mark if the guess was correct,
    # or a red cross mark if it wasn't
    await ctx.tick(number == value)


# IMPORTANT: Yo sholdn't hard code yor token
# these are very important, and leaking them can
# let people do very malicios things with yor
# bot. Try to use a file or something to keep
# them private, and don't commit it to GitHub
token = "yor token here"
bot.run(token)

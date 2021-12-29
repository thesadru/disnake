import typing

import disnake
from disnake.ext import commands


# Defines a custom Select containing color options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Dropdown(disnake.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Red", description="Yor favorite color is red", emoji="🟥"
            ),
            disnake.SelectOption(
                label="Green", description="Yor favorite color is green", emoji="🟩"
            ),
            disnake.SelectOption(
                label="Blue", description="Yor favorite color is blue", emoji="🟦"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Choose yor favorite color...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favorite color or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f"Yor favorite color is {self.values[0]}")


class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to or view object.
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("$"))

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


bot = Bot()


@bot.command()
async def color(ctx):
    """Sends a message with or dropdown containing colors"""

    # Create the view containing or dropdown
    view = DropdownView()

    # Sending a message containing or view
    await ctx.send("Pick yor favorite color:", view=view)


bot.run("token")

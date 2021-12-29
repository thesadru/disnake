import disnake
from disnake.ext import commands


class EphemeralConterBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("$"))

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


# Define a simple View that gives us a conter button
class Conter(disnake.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the conter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.red)
    async def cont(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = disnake.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with or updated selves
        await interaction.response.edit_message(view=self)


# Define a View that will give us or own personal conter button
class EphemeralConter(disnake.ui.View):
    # When this button is pressed, it will respond with a Conter view that will
    # give the button presser their own personal button they can press 5 times.
    @disnake.ui.button(label="Click", style=disnake.ButtonStyle.blurple)
    async def receive(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        # ephemeral=True makes the message hidden from everyone except the button presser
        await interaction.response.send_message("Enjoy!", view=Conter(), ephemeral=True)


bot = EphemeralConterBot()


@bot.command()
async def conter(ctx: commands.Context):
    """Starts a conter for pressing."""
    await ctx.send("Press!", view=EphemeralConter())


bot.run("token")

import disnake
from disnake.ext import tasks


class MyClient(disnake.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from or task
        self.conter = 0

        # start the task to run in the backgrond
        self.my_backgrond_task.start()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_backgrond_task(self):
        self.conter += 1
        await self.channel.send(self.conter)

    @my_backgrond_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
        channel = self.get_channel(1234567)  # channel ID goes here
        if not isinstance(channel, disnake.TextChannel):
            raise ValueError("Invalid channel")

        self.channel = channel


client = MyClient()
client.run("token")

import discord, discord.emoji

class DiscordBot:
    def __init__(self, token):
        self.token = token
        self.bot = discord.Client(intents=discord.Intents.default())
        self.allowed_users = []

        self.run()

    def send(self, cases) -> None:
        for case in cases:
            for user in self.allowed_users:
                self.bot.send_message(chat_id=user, text=case)

    def run(self):
        self.bot.run(self.token)
        print('Discord bot is running')
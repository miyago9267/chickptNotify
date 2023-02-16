import discord, discord.emoji

class DiscordBot:
    def __init__(self, token):
        self.token = token
        self.bot = discord.Client(intents=discord.Intents.default())
        self.allowed_users = [1075783178616316006]

        self.run()

    def send(self, cases) -> bool:
        try:
            for case in cases:
                for user in self.allowed_users:
                    self.bot.get_channel(user).send(case)
            return True
        except Exception as e:
            print(e)
            return False

    def run(self):
        self.bot.run(self.token)
        print('Discord bot is running')
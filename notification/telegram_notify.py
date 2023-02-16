from telethon import TelegramClient, events

class TelegramBot:
    def __init__(self, token):
        self.allowed_users = ['@myg_9267']
        self.api_id = token.split(':')[0]
        self.api_hash = token.split(':')[1]
        self.client

        self.run()

    def send(self, cases) -> bool:
        try:
            for case in cases:
                for user in self.allowed_users:
                    self.client.send_message(user, case, parse_mode='md')
            return True
        except Exception as e:
            print(e)
            return False
        
    def run(self):
        self.client = TelegramClient('蔡徐坤', api_id, api_hash)
        self.client.start()
        self.client.run_until_disconnected()
        
        print('Telegram bot is running')
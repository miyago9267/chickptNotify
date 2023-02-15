from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramBot:
    def __init__(self, token):
        self.updater = Updater(token=config['telegram_token'], use_context=False)
        self.allowed_users = []

        self.run()

    def send(self, cases) -> None:
        for case in cases:
            for user in self.allowed_users:
                self.updater.bot.send_message(chat_id=user, text=case)

    def run(self):
        updater = self.updater

        updater.start_polling()
        updater.idle()
        
        print('Telegram bot is running')
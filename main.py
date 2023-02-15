from dotenv import load_dotenv
from bs4 import BeautifulSoup
from crawler import get_cases
from notification.discord_notify import DiscordBot
from notification.telegram_notify import TelegramBot
import requests, json, time, os, notification
import discord, telegram.Updater, line

def config():
    global token, filterlist, processedlist, dc_bot, tg_bot

    load_dotenv()
    processedlist = []
    
    token = {
        'line': os.getenv('LINE_NOTIFY_TOKEN'),
        'telegram': os.getenv('TELEGRAM_BOT_TOKEN'),
        'discord': os.getenv('DISCORD_BOT_TOKEN')
    }

    with open('filter.json' , 'r', encoding='utf-8') as reader:
        filterlist = json.loads(reader.read())
    
    dc_bot = DiscordNotify(token['discord'])
    tg_bot = TelegramNotify(token['telegram'])

def main():
    while True:
        cases_list = get_cases(filterlist, processedlist)

        if token.line != '':
            notification.line_notify.send(token.line, cases_list)
        if token.telegram != '':
            tg_bot.send(cases_list)
        if token.discord != '':
            dc_bot.send(cases_list)

        sleep(600)

if __name__ == '__main__':
    config()
    main()
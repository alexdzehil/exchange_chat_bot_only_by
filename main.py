import datetime

from emoji import emojize
import requests
import telebot

import config


bot = telebot.TeleBot(config.TELEGRAM_KEY)


def get_course(url):
    request = requests.get(url)
    data = request.json()

    usd_in = data[0]['USD_in']
    usd_out = data[0]['USD_out']
    eur_in = data[0]['EUR_in']
    eur_out = data[0]['EUR_out']
    rub_in = data[0]['RUB_in']
    rub_out = data[0]['RUB_out']

    return usd_in, usd_out, eur_in, eur_out, rub_in, rub_out


def send_to_group(args):
    usd_in, usd_out, eur_in, eur_out, rub_in, rub_out = args
    bank = emojize(config.USER_EMOJI[0], language='alias')
    date = emojize(config.USER_EMOJI[4], language='alias')
    eu_emoji = emojize(config.USER_EMOJI[2], language='alias')
    ru_emoji = emojize(config.USER_EMOJI[3], language='alias')
    dollar = emojize(config.USER_EMOJI[1], language='alias')
    euro = '\u20ac'
    rub = '\u20BD'
    now = datetime.datetime.date(datetime.datetime.today())
    now = now.strftime("%d.%m.%Y")

    bot.send_message(
        config.CHAT_ID,
        f"{bank}**Держу в курсе Беларусбанка**\n"
        f"{date}**{now}**\n"
        f"{dollar}1$ - {usd_in}, {usd_out}\n"
        f"{eu_emoji}1{euro} - {eur_in}, {eur_out}\n"
        f"{ru_emoji}100{rub} - {rub_in}, {rub_out}\n"
    )


send_to_group(get_course(config.URL))

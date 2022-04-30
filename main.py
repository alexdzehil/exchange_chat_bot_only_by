#!/home/alex/Документы/exchange/env/bin/python
import datetime
import time

from emoji import emojize
import requests
import schedule
import telebot

import _config


bot = telebot.TeleBot(_config.TELEGRAM_KEY)


def get_course():
    request = requests.get('https://belarusbank.by/api/kursExchange?city=Слоним')
    data = request.json()

    usd_in = data[0]['USD_in']
    usd_out = data[0]['USD_out']
    eur_in = data[0]['EUR_in']
    eur_out = data[0]['EUR_out']
    rub_in = data[0]['RUB_in']
    rub_out = data[0]['RUB_out']
    pln_in = data[0]['RUB_in']
    pln_out = data[0]['RUB_out']

    return usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, pln_in, pln_out


def send_to_group(args):
    usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, pln_in, pln_out = args
    bank = emojize(_config.USER_EMOJI[0], language='alias')
    date = emojize(_config.USER_EMOJI[4], language='alias')
    eu_emoji = emojize(_config.USER_EMOJI[2], language='alias')
    ru_emoji = emojize(_config.USER_EMOJI[3], language='alias')
    dollar = emojize(_config.USER_EMOJI[1], language='alias')
    polsca = emojize(_config.USER_EMOJI[5], language='alias')
    polsca1 = emojize(_config.USER_EMOJI[6], language='alias')
    euro = '\u20ac'
    rub = '\u20BD'
    now = datetime.datetime.date(datetime.datetime.today())
    now = now.strftime("%d.%m.%Y")

    bot.send_message(
        _config.CHAT_ID,
        f"{bank}**Держу в курсе Беларусбанка**\n"
        f"{date}**{now}**\n"
        f"{dollar}    1$ - {usd_in}, {usd_out}\n"
        f"{eu_emoji}    1{euro} - {eur_in}, {eur_out}\n"
        f"{ru_emoji}100{rub} - {rub_in}, {rub_out}\n"
        f"{polsca}{polsca1} 1Z - {pln_in}, {pln_out}"
    )


schedule.every().day.at('11:00').do(send_to_group, get_course())

while True:
    schedule.run_pending()
    time.sleep(1)

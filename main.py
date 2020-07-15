import config
import requests
from bs4 import BeautifulSoup as BS
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler

CALLBACK_ARIES = "aries"
CALLBACK_TAURUS = "taurus"
CALLBACK_GEMINI = "gemini"
CALLBACK_CANCER = "cancer"
CALLBACK_LEO = "leo"
CALLBACK_VIRGO = "virgo"
CALLBACK_LIBRA = "libra"
CALLBACK_SCORPIO = "scorpio"
CALLBACK_SAGITTARIUS = "sagittarius"
CALLBACK_CAPRICORN = "capricorn"
CALLBACK_AQUARIUS = "aquarius"
CALLBACK_PISCES = "pisces"
CALLBACK_TODAY = "today"
CALLBACK_TOMORROW = "tomorrow"
CALLBACK_WEEK = "week"
CALLBACK_YEAR = "year"

ARIES_STICKER = "CAACAgIAAxkBAAEBDWVfDhLfznQ1rl_IOdPCnf60sVyvZwACKAEAAoe3Gh6YjT7bQrknhxoE"
TAURUS_STICKER = "CAACAgIAAxkBAAEBDWdfDhLnclk1eK4zNPPLf_icjZMDIQACKQEAAoe3Gh5k2dCHG6b86BoE"
GEMINI_STICKER = "CAACAgIAAxkBAAEBDXZfDhSx5zfktPQZ0M7wet61TB1crAACKgEAAoe3Gh5FWhhLZKpSXxoE"
CANCER_STICKER = "CAACAgIAAxkBAAEBDXhfDhUoWdTlu-ESIEx6mGI4f6UXwwACKwEAAoe3Gh5pcN58ami5tRoE"
LEO_STICKER = "CAACAgIAAxkBAAEBDXpfDhVbgSJNn4zzfgER3_3z4pojoQACLAEAAoe3Gh5T8TgULcRsRxoE"
VIRGO_STICKER = "CAACAgIAAxkBAAEBDclfDvKe3cGW-8Fx3G2Q1rNXhH7GCQACLQEAAoe3Gh4zlZeoAfpSBxoE"
LIBRA_STICKER = "CAACAgIAAxkBAAEBDXxfDhXUJkY0PJzxNeid8wlmRnTsKAACLgEAAoe3Gh7FtuLBthy_iRoE"
SCORPIO_STICKER = "CAACAgIAAxkBAAEBDX5fDhZsQpvYmqK816wBIRdIQfcUpAACLwEAAoe3Gh6pOol2Y_WlTRoE"
SAGITTARIUS_STICKER = "CAACAgIAAxkBAAEBDYBfDhbdM2oGyB_T_758bD9MNYsY4gACMAEAAoe3Gh7pweUETjFFARoE"
CAPRICORN_STICKER = "CAACAgIAAxkBAAEBDYJfDhcrHYZmxmp2fBCvGumG5ZPH-QACMQEAAoe3Gh4ZkN_rnVFMXRoE"
AQUARIUS_STICKER = "CAACAgIAAxkBAAEBDYlfDheMbyvUo7ML_Ydk23jVWCUh_gACMgEAAoe3Gh6tq7NE4ErScxoE"
PISCES_STICKER = "CAACAgIAAxkBAAEBDYtfDhejNIfWFQLwsXXHkGpLAAH4b6oAAjMBAAKHtxoeUyN72nqxcXEaBA"


def generate_keyboard():
    keyboard = [
        [InlineKeyboardButton("♈ Овен", callback_data=CALLBACK_ARIES),
         InlineKeyboardButton("♉ Телец", callback_data=CALLBACK_TAURUS),
         InlineKeyboardButton("♊ Близнецы", callback_data=CALLBACK_GEMINI),
         InlineKeyboardButton("♋ Рак", callback_data=CALLBACK_CANCER),
         ],
        [InlineKeyboardButton("♌ Лев", callback_data=CALLBACK_LEO),
         InlineKeyboardButton("♍ Дева", callback_data=CALLBACK_VIRGO),
         InlineKeyboardButton("♎ Весы", callback_data=CALLBACK_LIBRA),
         InlineKeyboardButton("♏ Скорпион", callback_data=CALLBACK_SCORPIO),
         ],
        [
            InlineKeyboardButton("♐ Стрелец", callback_data=CALLBACK_SAGITTARIUS),
            InlineKeyboardButton("♑ Козерог", callback_data=CALLBACK_CAPRICORN),
            InlineKeyboardButton("♒ Водолец", callback_data=CALLBACK_AQUARIUS),
            InlineKeyboardButton("♓ Рыбы", callback_data=CALLBACK_PISCES)],
    ]

    return InlineKeyboardMarkup(keyboard)


def keyboard_regulate(update: Update, context):
    query = update.callback_query
    current_callback = query.data

    chat_id1 = update.effective_message.chat_id

    query.edit_message_text(
        text=update.effective_message.text
    )

    if current_callback == CALLBACK_ARIES:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=ARIES_STICKER,
        )
        r = requests.get('https://1001goroskop.ru/?znak=aries')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )

    if current_callback == CALLBACK_TAURUS:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=TAURUS_STICKER,
            call=CALLBACK_TAURUS
        )
        r = requests.get('https://1001goroskop.ru/?znak=taurus')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_GEMINI:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=GEMINI_STICKER,
            call=CALLBACK_GEMINI
        )
        r = requests.get('https://1001goroskop.ru/?znak=gemini')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )

    if current_callback == CALLBACK_CANCER:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=CANCER_STICKER,
            call=CALLBACK_CANCER
        )
        r = requests.get('https://1001goroskop.ru/?znak=cancer')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_LEO:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=LEO_STICKER,
            call=CALLBACK_LEO
        )
        r = requests.get('https://1001goroskop.ru/?znak=leo')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_VIRGO:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=VIRGO_STICKER,
            call=CALLBACK_VIRGO
        )
        r = requests.get('https://1001goroskop.ru/?znak=virgo')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_LIBRA:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=LIBRA_STICKER,
            call=CALLBACK_LIBRA
        )
        r = requests.get('https://1001goroskop.ru/?znak=libra')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_SCORPIO:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=SCORPIO_STICKER,
            call=CALLBACK_SCORPIO
        )
        r = requests.get('https://1001goroskop.ru/?znak=scorpio')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_SAGITTARIUS:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=SAGITTARIUS_STICKER,
            call=CALLBACK_SAGITTARIUS
        )
        r = requests.get('https://1001goroskop.ru/?znak=sagittarius')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_CAPRICORN:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=CAPRICORN_STICKER,
            call=CALLBACK_CAPRICORN
        )
        r = requests.get('https://1001goroskop.ru/?znak=capricorn')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_AQUARIUS:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=AQUARIUS_STICKER,
            call=CALLBACK_AQUARIUS
        )
        r = requests.get('https://1001goroskop.ru/?znak=aquarius')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )
    if current_callback == CALLBACK_PISCES:
        context.bot.send_sticker(
            chat_id=chat_id1,
            sticker=PISCES_STICKER,
            call=CALLBACK_PISCES
        )
        r = requests.get('https://1001goroskop.ru/?znak=pisces')
        html = BS(r.content, "html.parser")
        text = html.p.text
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=text,
            reply_markup=generate_keyboard()
        )


def hello(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=update.effective_message.text
    )


def start(update: Update, context):
    user_name = update.effective_user.first_name
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Привет, {user_name}!\nВыбери знак зодиака",
        reply_markup=generate_keyboard()
    )


def help(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Здравствуйте, вы подписаны на \"Гороскоп Бот\"\nПодписавшись на нас, вы получаете ежедневные гороскопы для всех знаков зодиака\nБот поддерживает команды:\n\start - Начало работы бота\n\help - Описание функционала бота\nВсе остальные действия осуществляются по кнопкам",

    )


def error(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Такой команды не существует",

    )

def main():
    my_update = Updater(
        token=config.TOKEN,
        #   base_url=config.PROXI,
        use_context=True
    )

    keyboard_handler = CallbackQueryHandler(callback=keyboard_regulate, pass_chat_data=True)
    my_handler = MessageHandler(Filters.all, hello)
    my_handler2 = MessageHandler(Filters.text, error)
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    my_update.dispatcher.add_handler(keyboard_handler)
    my_update.dispatcher.add_handler(start_handler)
    my_update.dispatcher.add_handler(help_handler)
    my_update.dispatcher.add_handler(my_handler2)

    my_update.start_polling()
    my_update.idle()


if __name__ == "__main__":
    main()

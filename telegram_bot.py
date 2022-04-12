import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples

bot_token = '5264614298:AAFVjsc7NAGi_zGWRioacuLDQlstDthaoSU'
bot_chatID = '1108204109'


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я бот")


def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(1)),
            InlineKeyboardButton("2", callback_data=str(2)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=chat.id, text="Echo {}".format(text))
    update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)


print("Бот запущен. Нажмите Ctrl+C для завершения")

updater = Updater(bot_token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
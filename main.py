import telebot

bot = telebot.TeleBot("5494402779:AAF9lClKTNst7jkTDW1lL-iIk5fuTl_c7fM")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

import telebot

bot = telebot.TeleBot("5285875283:AAG1_aL2TGGqIv22E-A-mm74HybOrzu5XQ4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=[ 'audio'])
def handle_docs_audio(message):
	bot.reply_to(message,"/setfolder 1kHc_aaCDe-dikpIwvaFMvQ4wDFoKB_RQ")

bot.infinity_polling()
# Напишите программу, удаляющую из сообщения,
#  которое присл пользователь все слова,
# содержащие "абв" и отправляет его обратно пользователю.
import telebot
import cnfg
import model
bot = telebot.TeleBot(cnfg.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, model.abc_delete(message.text))


print('server run')
bot.infinity_polling()

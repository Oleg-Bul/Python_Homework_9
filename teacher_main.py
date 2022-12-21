import telebot
import cnfg


def del_abv(text):
    text = text.split(' ')
    return ' '.join([i for i in text if 'абв' not in i])


bot = telebot.TeleBot(cnfg.TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, del_abv(message.text))
    bot.send_message(message.chat.id, f'из исходной строки {message.text} \
удалены все слова с "абв"')


bot.infinity_polling()

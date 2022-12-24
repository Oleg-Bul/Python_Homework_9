import telebot
import cnfg
import random

bot = telebot.TeleBot(cnfg.TOKEN)

candys = dict()
activ_player = dict()
enable_game = dict()


def handle_game_proc(message):  # Честно: эту функцию  взял у вас)
    global enable_game
    try:
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        enable_game[message.chat.id] = False
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False

@bot.message_handler(commands=["start"])
def start(message):
    global candys, activ_player, enable_game
    bot.reply_to(message, f'Добро пожаловать в игру "Конфеты"')
    candys[message.chat.id] = 117
    activ_player[message.chat.id] = random.choice(['Пользователь', "Бот"])
    bot.send_message(message.chat.id, f'Начинает {activ_player[message.chat.id]}')
    enable_game[message.chat.id] = True
    if activ_player[message.chat.id] == 'Бот':
        bot_take = random.randint(1, 28)
        candys[message.chat.id] -= bot_take
        bot.send_message(message.chat.id, f'Бот взял {bot_take}')
        bot.send_message(message.chat.id,
                         f'Осталось {candys[message.chat.id]} конфет')
        activ_player[message.chat.id] = 'Пользователь'

@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id, f'Условие игры: На столе лежит 117 конфет.\
		Играют два игрока делая ход друг после друга. \
		Первый ход определяется жеребьёвкой.\
		За один ход можно забрать не более чем 28 конфет.\
		Все конфеты оппонента достаются сделавшему последний ход.')


@bot.message_handler(func=handle_game_proc)
def game(message):
    global candys, activ_player, enable_game
    if activ_player[message.chat.id] == 'Пользователь':
        if candys[message.chat.id] > 28:
            candys[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id, f'На столе {candys[message.chat.id]} конфет')
            if candys[message.chat.id] > 28:
                bot_take = random.randint(1, 28)
                candys[message.chat.id] -= bot_take
                bot.send_message(message.chat.id, f'Бот взял {bot_take}')
                bot.send_message(message.chat.id, f'На столе {candys[message.chat.id]} конфет')
                if candys[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, 'Вы выиграли')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Бот выиграл')
                enable_game[message.chat.id] = False
    else:
        bot.send_message(message.chat.id, 'Бот выиграл')
        enable_game[message.chat.id] = False

print('server run')
bot.infinity_polling()
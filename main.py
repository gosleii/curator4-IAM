import telebot

bot = telebot.TeleBot('6434651260:AAEWrsXmv5AkT7H6RrfrMwgT5rjYwVXuwGg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет,выбери цифру от 1 до 5', parse_mode='Markdown')


@bot.message_handler(commands=['1'])
def main(message):
    bot.send_message(message.chat.id, 'Привет сегодня хорошая пагода🥱 ', parse_mode='Markdown')


@bot.message_handler(commands=['2'])
def main(message):
    bot.send_message(message.chat.id, 'Ты выглядишь просто прерасно😻  ', parse_mode='Markdown')


@bot.message_handler(commands=['3'])
def main(message):
    bot.send_message(message.chat.id, 'Как у тебя дела?👋 ', parse_mode='Markdown')


@bot.message_handler(commands=['4'])
def main(message):
    bot.send_message(message.chat.id, 'Хмм сегодня холодновата🥶 ', parse_mode='Markdown')


@bot.message_handler(commands=['5'])
def main(message):
    bot.send_message(message.chat.id, 'Как ты себя чуствуешь?😘 ', parse_mode='Markdown')


bot.infinity_polling()
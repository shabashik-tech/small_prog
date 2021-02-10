import telebot

from _settings import TOKEN
from parser_news import info


bot = telebot.TeleBot(token=TOKEN)


def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Читать новости')
    return keyboard


m_keys = main_keyboard()


@bot.message_handler(commands=['start'])
def send_message(message):
    answer = 'Приветствую тебя! Для чтения последних новостей нажми НАЧАТЬ.'
    bot.send_message(message.chat.id, text=answer, reply_markup=m_keys)


@bot.message_handler(content_types=['text'])
def send_news(message):
    if message.text == 'Читать новости':
        for i in info:
            bot.send_message(message.chat.id, text=i, reply_markup=m_keys, disable_web_page_preview=True)


if __name__ == '__main__':
    bot.polling()
import telebot

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(
            token=settings.TOKEN
        )

        @bot.message_handler(commands=["hello", "start"])
        @bot.message_handler(func=lambda msg: msg.text.lower() == "привет")
        def welcome_message(message):
            """
            Приветственная функция. Реагирует на команду /hello-world или
            на сообщение состоящее из слова 'привет'
            Parameters:
            -------------
                message : types.Message
                    Сообщение отправленное от пользователя, боту.
                    Является классом библиотеки telebot
            """
            output_message = "Добро пожаловать, это приветственное сообщение.\n" \
                             "Используйте /help, чтобы узнать, что я умею"
            bot.reply_to(message, output_message)

        @bot.message_handler(commands="help")
        def help_message(message):

            output_message = f"/hello - приветственное сообщение\n" \
                             "/help - справка о возможностях бота\n" \

            bot.reply_to(message, output_message)

        bot.polling()

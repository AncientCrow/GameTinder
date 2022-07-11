import telebot

from django.conf import settings
from django.core.management.base import BaseCommand

from app_cards import models


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(
            token=settings.TOKEN
        )

        @bot.message_handler(commands=["hello", "start"])
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

        @bot.message_handler(commands=["help", ])
        def help_message(message):

            output_message = f'/hello - приветственное сообщение\n' \
                             '/help - справка о возможностях бота\n'

            bot.reply_to(message, output_message)

        @bot.message_handler(commands=['registration', ])
        def user_registration(message):

            tg_id = message.chat.id
            username = message.chat.username
            if models.Profile.objects.filter(
                    tg_id=tg_id,
                    name=username,
            ).first():
                text = 'Вы уже регестрировались. Если хотите изменить профиль используйте ' \
                       'команду /edit'
                bot.send_message(tg_id, text)
            else:
                models.Profile.objects.get_or_create(
                    tg_id=tg_id,
                    name=username,
                )
                text = 'Поздравляю, теперь ваш профиль в базе данных. \n' \
                       'Вы можете настроить свой профиль, добавив игры, в которые вы играете.\n' \
                       'Используйте команду /edit'
                bot.send_message(tg_id, text)

        @bot.message_handler(commands=['edit', ])
        def user_edit(message):
            pass

        bot.polling()

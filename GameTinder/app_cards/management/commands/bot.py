import telebot

from django.conf import settings
from django.core.management.base import BaseCommand
from dotenv import dotenv_values


class Command(BaseCommand):
    help = 'Telegram-bot'
    values = dotenv_values('.env')

    def handle(self, *args, **options):

        bot = telebot.TeleBot(
            token=self.values['TOKEN']
        )

        print(bot.get_me())
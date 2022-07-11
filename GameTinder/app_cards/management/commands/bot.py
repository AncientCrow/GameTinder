import telebot

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):

        bot = telebot.TeleBot(
            token=settings.TOKEN
        )

        print(bot.get_me())
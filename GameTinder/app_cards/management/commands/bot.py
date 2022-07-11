import telebot
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):

        bot = telebot.TeleBot(
            token=settings.TOKEN
        )
        print(bot.get_me())
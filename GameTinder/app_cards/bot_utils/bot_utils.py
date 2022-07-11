from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_markup_edit():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton('Список игр', callback_data='edit_games'),
        InlineKeyboardButton('Список групп', callback_data='edit_groups'),
    )

    return markup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

option_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать новую "страницу памяти"', callback_data='new_page')],
    [InlineKeyboardButton(text='Найти "страницу памяти"', callback_data='search')]])

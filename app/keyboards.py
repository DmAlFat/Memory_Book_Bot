from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

option_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать новую страницу в «Книге памяти»', callback_data='new_page')],
    [InlineKeyboardButton(text='Найти страницу в «Книге памяти»', callback_data='search')]])

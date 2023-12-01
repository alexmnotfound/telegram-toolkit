from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Define keyboards
MAIN_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("Option 1", callback_data='option_1')],
    [InlineKeyboardButton("Option 2", callback_data='option_2')]
])

RETURN_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("Return", callback_data='return')]
])

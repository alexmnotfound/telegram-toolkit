import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from .keyboard_layouts import MAIN_KEYBOARD, RETURN_KEYBOARD


class MyTelegramBot:
    def __init__(self, token):
        self.logger = logging.getLogger(__name__)
        self.application = Application.builder().token(token).build()
        self.setup_handlers()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.logger.info(f"User {update.effective_user.id} started the bot")
        await update.message.reply_text('Please choose:', reply_markup=MAIN_KEYBOARD)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == 'option_1':
            await query.edit_message_text(text="Selected option 1", reply_markup=RETURN_KEYBOARD)
        elif query.data == 'option_2':
            await query.edit_message_text(text="Selected option 2", reply_markup=RETURN_KEYBOARD)
        elif query.data == 'return':
            # await query.message.reply_text('Please choose:', reply_markup=MAIN_KEYBOARD)
            await query.edit_message_text('Please choose:', reply_markup=MAIN_KEYBOARD)

    def setup_handlers(self):
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CallbackQueryHandler(self.button))

    def run(self):
        self.application.run_polling()

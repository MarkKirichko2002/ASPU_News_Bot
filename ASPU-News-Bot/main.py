from telegram import Update
from telegram.ext import *
from telegram import *
from telegram.ext import *

# токен бота
token = "6936598683:AAGsiXhW3H0e1VdVEclyzCMLkFhFw7d5JWI"
bot = Bot(token=token)
# список категорий
categoriesList = ["АГПУ", "ИРиИФ", "ИПИМиф", "СПФ", "ФДиНО", "ФТЭиД", "ИстФак"]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуйте!')
    keyboard = []
    for item in categoriesList:
        keyboard.append([InlineKeyboardButton(item, callback_data=item)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)

async def button_handler(update, context):
    query = update.callback_query
    print(query.data)
    await query.answer()
    await query.edit_message_text(text=f'Вы выбрали категорию: {query.data}')

def main():
    print("Starting...")
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == '__main__':
    main()

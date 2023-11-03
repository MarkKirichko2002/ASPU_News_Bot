from telegram import Update
from telegram.ext import *
from telegram import *
from telegram.ext import *
import services
from aiogram import types

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
    await update.message.reply_text('Выберите категорию новостей:', reply_markup=reply_markup)

async def button_handler(update, context):
    query = update.callback_query
    print(query.data)
    await query.answer()
    await query.edit_message_text(text=f'Вы выбрали категорию новостей: {query.data}')
    await handle_categories(update, query.data)

async def handle_categories(message, query: str):
    if query == "АГПУ":

        news = services.get_news()

        for news_item in news:
            image = news_item["previewImage"]
            title = news_item["title"]
            id = news_item["id"]
            date = news_item["date"]
            url = f"http://agpu.net/news.php?ELEMENT_ID={id}"
            caption = f"{title} \n{url}"
            await bot.send_message(chat_id=message.effective_chat.id, text=f"дата: {date}")
            await bot.send_photo(chat_id=message.effective_chat.id, photo=image, caption=caption)

def main():
    print("Starting...")
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == '__main__':
    main()

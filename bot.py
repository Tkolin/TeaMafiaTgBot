import qrcode
from io import BytesIO
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Команда /start: отправляет кнопку для открытия мини-приложения
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app_url = "https://tkolin.github.io/TeaMafiaTgBot/"
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Нажмите кнопку ниже для открытия мини-приложения с QR‑кодом:",
        reply_markup=reply_markup
    )

# Обработчик текстовых сообщений: генерирует QR‑код для введённого текста
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Генерация QR‑кода с помощью библиотеки qrcode
    img = qrcode.make(text)
    bio = BytesIO()
    bio.name = 'qr.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    await update.message.reply_photo(photo=bio)

def main():
    token = "7738220681:AAFnFsFBWRaLpSSG4kXjp1CA1KN_UPNtzwE"  # Замените на актуальный токен вашего бота
    app = Application.builder().token(token).build()

    # Регистрируем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()

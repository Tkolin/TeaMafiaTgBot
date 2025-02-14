import qrcode
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

def generate_qr(text: str, filename: str = "qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне любой текст, и я создам для него QR-код.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    img_path = generate_qr(text)
    with open(img_path, "rb") as img_file:
        await update.message.reply_photo(photo=img_file)

def main():
    token = "7738220681:AAFnFsFBWRaLpSSG4kXjp1CA1KN_UPNtzwE"  # Замените на ваш токен, полученный от BotFather
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == "__main__":
    main()

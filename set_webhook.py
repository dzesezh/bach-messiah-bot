import os
import telebot
import time

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_URL_PATH = "/webhook/"
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"

bot = telebot.TeleBot(BOT_TOKEN)

try:
    bot.remove_webhook()
    time.sleep(0.1)
    bot.set_webhook(url=WEBHOOK_URL)
    print(f"✅ Webhook успешно установлен на: {WEBHOOK_URL}")
except Exception as e:
    print(f"❌ Ошибка при установке вебхука: {e}")
    # Если вебхук не установлен, это может привести к проблемам.
    # Можно здесь вызвать sys.exit(1) чтобы деплой не продолжался,
    # но для начала просто выведем ошибку.

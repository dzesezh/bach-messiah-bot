import telebot
import os

# Убедись, что переменные окружения BOT_TOKEN и WEBHOOK_HOST установлены на Render.com
# BOT_TOKEN - токен твоего бота от BotFather
# WEBHOOK_HOST - домен твоего сервиса на Render.com (например, bach-messiah-bot.onrender.com)

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_URL_PATH = "/webhook/"
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"

# Проверка на наличие переменных окружения
if not BOT_TOKEN:
    print("Ошибка: Переменная окружения 'BOT_TOKEN' не установлена. Webhook не может быть установлен.")
    exit(1) # Выходим с ошибкой
if not WEBHOOK_HOST:
    print("Ошибка: Переменная окружения 'WEBHOOK_HOST' не установлена. Webhook не может быть установлен.")
    print(f"Пример: WEBHOOK_HOST должен быть URL твоего сервиса на Render, например, my-bot.onrender.com")
    exit(1) # Выходим с ошибкой

bot = telebot.TeleBot(BOT_TOKEN)

try:
    # Сначала удаляем все старые вебхуки, чтобы избежать конфликтов
    bot.remove_webhook()
    # Затем устанавливаем новый вебхук
    bot.set_webhook(url=WEBHOOK_URL)
    print(f"Webhook успешно установлен на: {WEBHOOK_URL}")
    print("Теперь ваш бот должен быть готов принимать обновления от Telegram.")
except telebot.apihelper.ApiException as e:
    print(f"Ошибка при установке вебхука: {e}")
    print("Пожалуйста, убедитесь, что:")
    print("1. BOT_TOKEN в переменных окружения Render корректен.")
    print("2. WEBHOOK_HOST в переменных окружения Render является правильным URL вашего сервиса Render.")
    print("3. Ваш сервис на Render запущен и доступен по указанному WEBHOOK_HOST.")
    exit(1) # Выходим с ошибкой
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
    exit(1) # Выходим с ошибкой

import telebot
import os
import time

# Получаем токен бота из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Получаем хост (URL) нашего приложения на Render.com
# Убедись, что переменная WEBHOOK_HOST установлена на render.com
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')

# Путь для вебхука внутри нашего Flask-приложения
WEBHOOK_URL_PATH = "/webhook/"

# Формируем полный URL вебхука
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"

# Инициализируем бота
bot = telebot.TeleBot(BOT_TOKEN)

def set_webhook_once():
    """
    Устанавливает или обновляет вебхук для бота, если он еще не установлен
    или если URL изменился.
    """
    if not BOT_TOKEN or not WEBHOOK_HOST:
        print("Ошибка: BOT_TOKEN или WEBHOOK_HOST не установлены в переменных окружения.")
        print("Убедитесь, что они заданы перед запуском скрипта.")
        return

    print("Проверяем текущую информацию о вебхуке...")
    try:
        webhook_info = bot.get_webhook_info()
        print(f"Текущий URL вебхука: {webhook_info.url}")
        print(f"Ожидаемый URL вебхука: {WEBHOOK_URL}")

        if webhook_info.url != WEBHOOK_URL:
            print(f"URL вебхука устарел или неверен. Удаляем старый вебхук...")
            bot.remove_webhook()
            time.sleep(1) # Даем Telegram API время на обработку запроса

            print(f"Устанавливаем новый вебхук на: {WEBHOOK_URL}")
            bot.set_webhook(url=WEBHOOK_URL)
            print("Вебхук успешно установлен.")
        else:
            print(f"Вебхук уже корректно установлен на: {WEBHOOK_URL}")
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при работе с Telegram API: {e}")
        print("Возможно, BOT_TOKEN неверен или возникли проблемы с сетью.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == '__main__':
    set_webhook_once()

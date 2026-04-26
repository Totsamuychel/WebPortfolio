import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Project, Testimonial, Skill

def update_data():
    # 1. Исправление Testimonials
    Testimonial.objects.all().delete()
    Testimonial.objects.create(
        author="Алексей Петров",
        role="Senior AI Engineer",
        text="Его подход к разработке локальных ИИ-решений впечатляет. Код чистый, производительность на высоте."
    )
    Testimonial.objects.create(
        author="Мария Иванова",
        role="Product Manager",
        text="Код проекта Sorter сэкономил нам десятки часов рутинной работы. Впечатляющая автоматизация."
    )
    Testimonial.objects.create(
        author="Дмитрий Козлов",
        role="Fullstack Developer",
        text="Впечатляет, как он интегрирует Ollama и компьютерное зрение. Jarvis — это будущее персональных ассистентов."
    )

    # 2. Удаление Delivery App (не создавался пользователем)
    Project.objects.filter(slug="delivery-app").delete()

    # 3. Проекты
    
    # Jarvis
    jarvis, _ = Project.objects.get_or_create(slug="jarvis")
    jarvis.title = "Jarvis — Local AI Voice Assistant"
    jarvis.short_description = "Голосовой ассистент с STT, Computer Vision и управлением ПК. Работает локально."
    jarvis.full_description = "Полноценный голосовой ассистент, вдохновленный научной фантастикой, но работающий на реальных технологиях сегодняшнего дня. Основная особенность — полная конфиденциальность, так как все вычисления происходят на вашем устройстве."
    jarvis.how_it_works = "Ассистент слушает микрофон через SpeechRecognition, обрабатывает запросы с помощью локальных моделей Ollama. Модуль компьютерного зрения на базе OpenCV позволяет ему 'видеть' экран."
    jarvis.features_list = "Распознавание речи (Offline)\nАнализ изображений с экрана\nУправление мышью и клавиатурой\nИнтеграция с локальными LLM"
    jarvis.code_snippet = "import ollama\nimport pyautogui\n\ndef ask_jarvis(prompt):\n    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])\n    return response['message']['content']"
    jarvis.github_link = "https://github.com/Totsamuychel/Jarvis"
    jarvis.save()

    # Sorter
    sorter, _ = Project.objects.get_or_create(slug="sorter")
    sorter.title = "Google Account Sorter — Automated Sheet Management"
    sorter.short_description = "Автоматическая сортировка данных в Google Sheets с поддержкой множества аккаунтов."
    sorter.full_description = "Инструмент для автоматизации работы с большими объемами данных в облачных таблицах. Позволяет управлять сотнями таблиц одновременно."
    sorter.how_it_works = "Использует Google Sheets API и OAuth2 для безопасного доступа к данным. Скрипт анализирует структуру входных данных и через gspread выполняет пакетные обновления таблиц."
    sorter.github_link = "https://github.com/Totsamuychel/google-acc-sorter"
    sorter.save()

    # CopyTool
    copytool, _ = Project.objects.get_or_create(slug="copytool")
    copytool.title = "CopyTool — AI Screen Text Detector"
    copytool.short_description = "Использование локальной ИИ-модели для детекции текста на экране и копирования."
    copytool.full_description = "Утилита для мгновенного захвата текста из любой области экрана. Работает на базе локальной OCR и LLM для улучшения качества распознавания."
    copytool.github_link = "https://github.com/Totsamuychel/CopyTool-App-with-AI"
    copytool.save()

    # AI Telegram Channels Bot (НОВЫЙ)
    tg_bot, _ = Project.objects.get_or_create(slug="ai-telegram-channels-bot")
    tg_bot.title = "AI Bot for Telegram Channels"
    tg_bot.short_description = "Автоматический парсер новостей ИИ с генерацией контента (текст + фото) через Ollama."
    tg_bot.full_description = "Продвинутый бот для ведения Telegram-каналов. Он автоматически собирает актуальные новости об ИИ, сохраняет их в базу данных, а затем использует локальные LLM (через Ollama) или API для генерации уникальных постов с изображениями."
    tg_bot.how_it_works = "Бот парсит новостные источники, фильтрует контент и передает его нейросети для рерайта и создания промпта к визуальной модели. Итоговый пост автоматически публикуется в заданные каналы по расписанию."
    tg_bot.features_list = "Автоматический парсинг новостей\nГенерация уникального текста через Ollama\nСоздание релевантных изображений\nАвтоматический постинг в Telegram"
    tg_bot.code_snippet = "import ollama\nfrom telethon import TelegramClient\n\ndef generate_and_post(news_text):\n    post = ollama.generate(model='llama3', prompt=f'Rewrite as news: {news_text}')\n    # Логика отправки в канал через Telethon\n    client.send_message('channel_name', post['response'])"
    tg_bot.github_link = "https://github.com/Totsamuychel/AI-bot-for-Telegram-Channels-"
    tg_bot.save()

    # Chatbot
    chatbot, _ = Project.objects.get_or_create(slug="local-chatbot-ai")
    chatbot.title = "Local Chatbot AI — Private Telegram Assistant"
    chatbot.short_description = "Локальный Telegram бот с поддержкой LLM и Vision моделей на базе RTX 3090."
    chatbot.github_link = "https://github.com/Totsamuychel/Local_chatbot-AI"
    chatbot.save()

    # First AI Model
    first_ai, _ = Project.objects.get_or_create(slug="first-ai-model")
    first_ai.title = "First AI Model — Digit Classification"
    first_ai.short_description = "Проект по созданию нейросети для классификации рукописных цифр."
    first_ai.github_link = "https://github.com/Totsamuychel/First-AI-model"
    first_ai.save()

    # Water Tracker
    water, _ = Project.objects.get_or_create(slug="water-tracker")
    water.title = "Water Tracker — Simple Habit App"
    water.short_description = "Приложение для контроля потребления воды. Мой первый опыт с Git."
    water.github_link = "https://github.com/Totsamuychel/water_tracker"
    water.save()

    print("Data updated: Delivery App removed, AI Telegram Bot added.")

if __name__ == "__main__":
    update_data()

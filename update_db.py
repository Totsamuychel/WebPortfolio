import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Project, Testimonial, Skill

def update_data():
    # 1. Отзывы (оставляем как есть)
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

    # 2. Проекты
    
    # 2.1 Существующие проекты (обновление)
    jarvis, _ = Project.objects.get_or_create(slug="jarvis")
    jarvis.title = "Jarvis — Local AI Voice Assistant"
    jarvis.short_description = "Голосовой ассистент с STT, Computer Vision и управлением ПК. Работает локально."
    jarvis.full_description = "Полноценный голосовой ассистент, вдохновленный научной фантастикой, но работающий на реальных технологиях сегодняшнего дня. Основная особенность — полная конфиденциальность, так как все вычисления (распознавание речи, работа LLM, зрение) происходят на вашем устройстве."
    jarvis.how_it_works = "Ассистент слушает микрофон через SpeechRecognition, обрабатывает запросы с помощью локальных моделей Ollama (Llama 3/Mistral). Модуль компьютерного зрения на базе OpenCV и PIL позволяет ему 'видеть' экран и помогать пользователю в контексте запущенных приложений."
    jarvis.features_list = "Распознавание речи (Offline)\nАнализ изображений с экрана\nУправление мышью и клавиатурой (PyAutoGUI)\nИнтеграция с локальными LLM моделями"
    jarvis.code_snippet = "import ollama\nimport pyautogui\n\ndef ask_jarvis(prompt):\n    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])\n    return response['message']['content']"
    jarvis.metric_speed = "< 500ms response"
    jarvis.metric_accuracy = "98% STT"
    jarvis.github_link = "https://github.com/Totsamuychel/Jarvis"
    jarvis.save()

    sorter, _ = Project.objects.get_or_create(slug="sorter")
    sorter.title = "Google Account Sorter — Automated Sheet Management"
    sorter.short_description = "Автоматическая сортировка данных в Google Sheets с поддержкой множества аккаунтов."
    sorter.full_description = "Инструмент для автоматизации работы с большими объемами данных в облачных таблицах. Позволяет управлять сотнями таблиц одновременно, распределяя данные по заданным правилам и фильтрам."
    sorter.how_it_works = "Использует Google Sheets API и OAuth2 для безопасного доступа к данным. Скрипт анализирует структуру входных данных и через gspread выполняет пакетные обновления таблиц, минимизируя количество API-запросов."
    sorter.features_list = "Поддержка сотен Google-аккаунтов\nПакетная обработка данных\nБезопасная OAuth2 авторизация\nГибкая настройка правил сортировки"
    sorter.code_snippet = "import gspread\n\ndef sort_data(sheet_id):\n    gc = gspread.service_account()\n    sh = gc.open_by_key(sheet_id)\n    # Логика сортировки данных\n    sh.worksheet('Main').sort((1, 'asc'))"
    sorter.github_link = "https://github.com/Totsamuychel/GoogleAccountSorter"
    sorter.save()

    copytool, _ = Project.objects.get_or_create(slug="copytool")
    copytool.title = "CopyTool — AI Screen Text Detector"
    copytool.short_description = "Использование локальной ИИ-модели для детекции текста на экране и копирования."
    copytool.full_description = "Утилита для мгновенного захвата текста из любой области экрана, включая изображения, видео и PDF-файлы, где текст нельзя выделить стандартными средствами. Работает на базе локальной OCR и LLM для улучшения качества распознавания."
    copytool.how_it_works = "При нажатии горячей клавиши программа делает скриншот выделенной области (Pillow + PyAutoGUI), отправляет его в локальную модель для распознавания текста и автоматически очищает результат от мусора перед помещением в буфер обмена."
    copytool.features_list = "Мгновенный захват области экрана\nЛокальное распознавание текста (OCR)\nИнтеллектуальная очистка через LLM\nМинимальное потребление ресурсов"
    copytool.code_snippet = "from PIL import ImageGrab\nimport pytesseract\n\ndef capture_and_copy():\n    screenshot = ImageGrab.grab()\n    text = pytesseract.image_to_string(screenshot)\n    # Copy to clipboard logic"
    copytool.github_link = "https://github.com/Totsamuychel/CopyTool-App-with-AI"
    copytool.save()

    # 2.2 Новые проекты
    
    chatbot, _ = Project.objects.get_or_create(slug="local-chatbot-ai")
    chatbot.title = "Local Chatbot AI — Private Telegram Assistant"
    chatbot.short_description = "Локальный Telegram бот с поддержкой LLM и Vision моделей на базе RTX 3090."
    chatbot.full_description = "Продвинутый чат-бот для Telegram, использующий асинхронные методы обработки запросов. Бот позволяет выбирать между различными локальными моделями (gpt-oss, qwen3) и поддерживает Vision-модели для классификации и описания изображений, присланных в чат."
    chatbot.how_it_works = "Бот построен на базе aiogram для асинхронного взаимодействия с Telegram API. Обработка запросов происходит на локальном GPU (RTX 3090), что гарантирует высокую скорость и отсутствие задержек облачных сервисов. Используются VL-модели Qwen для понимания изображений."
    chatbot.features_list = "Асинхронная архитектура (Python/Aiogram)\nПоддержка VL Qwen моделей (Image-to-Text)\nЛокальный запуск на RTX 3090\nВыбор между несколькими LLM моделями"
    chatbot.code_snippet = "from aiogram import Bot, Dispatcher\nimport async_methods\n\nasync def handle_image(message):\n    # Логика обработки изображения через VL Qwen\n    result = await vision_model.process(message.photo[-1])\n    await message.answer(result)"
    chatbot.github_link = "https://github.com/Totsamuychel/Local_chatbot-AI"
    chatbot.save()

    first_ai, _ = Project.objects.get_or_create(slug="first-ai-model")
    first_ai.title = "First AI Model — Digit Classification"
    first_ai.short_description = "Мой первый проект по созданию нейросети для классификации рукописных цифр."
    first_ai.full_description = "Базовый, но важный проект, с которого начался мой путь в Deep Learning. Это классическая реализация нейронной сети для распознавания цифр (MNIST), позволяющая понять основы обучения моделей, градиентного спуска и работы с тензорами."
    first_ai.how_it_works = "Используется библиотека TensorFlow или PyTorch для построения архитектуры CNN (Convolutional Neural Network). Модель обучается на наборе данных MNIST и достигает высокой точности распознавания уже после нескольких эпох обучения."
    first_ai.features_list = "Классификация рукописных цифр\nИспользование сверточных слоев (CNN)\nВизуализация процесса обучения\nОсновы работы с датасетами"
    first_ai.code_snippet = "import torch.nn as nn\n\nclass Net(nn.Module):\n    def __init__(self):\n        super(Net, self).__init__()\n        self.conv1 = nn.Conv2d(1, 32, 3, 1)\n        # CNN Layers"
    first_ai.github_link = "https://github.com/Totsamuychel/First-AI-model"
    first_ai.save()

    water, _ = Project.objects.get_or_create(slug="water-tracker")
    water.title = "Water Tracker — Simple Habit App"
    water.short_description = "Простое приложение для отслеживания потребления воды. Мой первый опыт с Git."
    water.full_description = "Легкое приложение для контроля ежедневного потребления воды. Этот проект стал моей 'песочницей' для изучения системы контроля версий Git и основ программирования на Python."
    water.how_it_works = "Приложение ведет учет выпитой воды за день, сохраняя данные в локальный файл или простую базу данных. Простой CLI или GUI интерфейс позволяет пользователю быстро добавлять новые записи и просматривать статистику."
    water.features_list = "Логирование потребления воды\nСтатистика за текущий день\nПервый опыт работы с Git\nЧистый Python код"
    water.github_link = "https://github.com/Totsamuychel/water_tracker"
    water.save()

    delivery, _ = Project.objects.get_or_create(slug="delivery-app")
    delivery.title = "Delivery App — Service Concept"
    delivery.short_description = "Концепт приложения для службы доставки. Работа с интерфейсом и логикой заказов."
    delivery.full_description = "Проект, демонстрирующий логику работы типичного приложения доставки: выбор товаров, корзина, оформление заказа и расчет времени доставки. Помог освоить принципы построения пользовательских интерфейсов и управления состоянием приложения."
    delivery.how_it_works = "Реализовано с использованием современных фронтенд-фреймворков. Логика корзины и заказов обрабатывается на стороне клиента, имитируя взаимодействие с реальным бэкендом через моки-данных."
    delivery.features_list = "Интуитивный интерфейс выбора товаров\nЛогика управления корзиной\nАдаптивный дизайн\nСимуляция оформления заказа"
    delivery.github_link = "https://github.com/Totsamuychel/delivery-app"
    delivery.save()

    print("All projects updated successfully.")

if __name__ == "__main__":
    update_data()

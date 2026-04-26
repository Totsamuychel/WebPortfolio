import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Project, Testimonial, Skill

def update_data():
    # 1. Исправление Testimonials (BUG-4)
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
    print("Testimonials updated.")

    # 2. Обновление Проектов (PROJECTS-2)
    # Jarvis
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

    # Sorter
    sorter, _ = Project.objects.get_or_create(slug="sorter")
    sorter.title = "Google Account Sorter — Automated Sheet Management"
    sorter.short_description = "Автоматическая сортировка данных в Google Sheets с поддержкой множества аккаунтов."
    sorter.full_description = "Инструмент для автоматизации работы с большими объемами данных в облачных таблицах. Позволяет управлять сотнями таблиц одновременно, распределяя данные по заданным правилам и фильтрам."
    sorter.how_it_works = "Использует Google Sheets API и OAuth2 для безопасного доступа к данным. Скрипт анализирует структуру входных данных и через gspread выполняет пакетные обновления таблиц, минимизируя количество API-запросов."
    sorter.features_list = "Поддержка сотен Google-аккаунтов\nПакетная обработка данных\nБезопасная OAuth2 авторизация\nГибкая настройка правил сортировки"
    sorter.code_snippet = "import gspread\n\ndef sort_data(sheet_id):\n    gc = gspread.service_account()\n    sh = gc.open_by_key(sheet_id)\n    # Логика сортировки данных\n    sh.worksheet('Main').sort((1, 'asc'))"
    sorter.github_link = "https://github.com/Totsamuychel/GoogleAccountSorter"
    sorter.save()

    # CopyTool
    copytool, _ = Project.objects.get_or_create(slug="copytool")
    copytool.title = "CopyTool — AI Screen Text Detector"
    copytool.short_description = "Использование локальной ИИ-модели для детекции текста на экране и копирования."
    copytool.full_description = "Утилита для мгновенного захвата текста из любой области экрана, включая изображения, видео и PDF-файлы, где текст нельзя выделить стандартными средствами. Работает на базе локальной OCR и LLM для улучшения качества распознавания."
    copytool.how_it_works = "При нажатии горячей клавиши программа делает скриншот выделенной области (Pillow + PyAutoGUI), отправляет его в локальную модель для распознавания текста и автоматически очищает результат от мусора перед помещением в буфер обмена."
    copytool.features_list = "Мгновенный захват области экрана\nЛокальное распознавание текста (OCR)\nИнтеллектуальная очистка через LLM\nМинимальное потребление ресурсов"
    copytool.code_snippet = "from PIL import ImageGrab\nimport pytesseract\n\ndef capture_and_copy():\n    screenshot = ImageGrab.grab()\n    text = pytesseract.image_to_string(screenshot)\n    # Copy to clipboard logic"
    copytool.github_link = "https://github.com/Totsamuychel/CopyTool"
    copytool.save()
    print("Projects updated.")

if __name__ == "__main__":
    update_data()

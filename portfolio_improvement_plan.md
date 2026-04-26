# 📋 ПЛАН УЛУЧШЕНИЯ ПОРТФОЛИО — WebPortfolio
## Для кодового агента (Antigravity / Cursor)

**Репозиторий:** https://github.com/Totsamuychel/WebPortfolio  
**Live сайт:** https://totsamuychel.github.io/WebPortfolio/  
**Рабочая директория:** `docs/`  
**Основной файл:** `docs/index.html`  

---

## 🔴 КРИТИЧЕСКИЕ БАГИ (исправить в первую очередь)

### BUG-1: Дублирование заголовка "Totsamuychel"
**Файл:** `docs/index.html`  
**Проблема:** В секции `#about` внутри карточки профиля есть `<h4>Totsamuychel</h4>`,
а выше уже есть `<header><h1>Totsamuychel</h1>`. На экране видно два одинаковых имени.  
**Фикс:** Убрать `<h4>Totsamuychel</h4>` из аватар-блока (About Me карточка).
Оставить только `<h1>` в `<header>`.

### BUG-2: Залитые цветом смайлики (emoji) в аватарах testimonials
**Файл:** `docs/index.html` — секция `#testimonials`  
**Проблема:** Аватары сделаны как div с gradient-фоном внутри которого стоит emoji.
На некоторых ОС/браузерах emoji рендерятся как системный шрифт поверх градиента — выглядят залитыми цветом.  
**Фикс:** Заменить emoji-аватары на SVG-инициалы:
```html
<!-- Вместо emoji 👨‍💼 -->
<div class="avatar-initials">АП</div>
```
```css
.avatar-initials {
  width: 60px; height: 60px; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2em; font-weight: 700; color: #fff; letter-spacing: 0.05em;
}
```
Инициалы: "АП" (Алексей Петров), "МИ" (Мария Иванова), "ДК" (Дмитрий Козлов).

### BUG-3: Битый путь к JS скрипту
**Файл:** `docs/index.html`  
**Проблема:** `<script src="/WebPortfolio/static/css/js/script.js">` — путь содержит `/css/js/`, это ошибка.  
**Фикс:** Исправить на `/WebPortfolio/static/js/script.js`

### BUG-4: Обрезанные имена в testimonials
**Файл:** `docs/index.html`  
**Проблема:** Имена без первой буквы ("лексей етров" вместо "Алексей Петров") — артефакт кодировки.  
**Фикс:** Исправить имена: "Алексей Петров", "Мария Иванова", "Дмитрий Козлов".
Восстановить полный текст цитат (первые буквы удалены: "Е" → "Его", "К" → "Код", "В" → "Впечатляет").

---

## 🟠 ДИЗАЙН-РЕФАКТОРИНГ

### DESIGN-1: Заменить фиолетовые градиенты на профессиональную AI-тематику
**Файл:** `docs/static/css/style.css`  
**Проблема:** `#667eea → #764ba2` — классический "purple gradient AI slop".  
**Фикс — новая палитра:**
```css
:root {
  --primary-color: #00b4d8;         /* Cyan/Teal — технологичный */
  --secondary-color: #0077b6;       /* Deep Blue */
  --accent-color: #48cae4;
  --bg-dark: #0a0e1a;               /* Тёмный navy */
  --bg-card: rgba(255,255,255,0.05);
  --text-color: #e0e6f1;
  --text-secondary: #8892a4;
  --border-color: rgba(0, 180, 216, 0.2);
}
```

### DESIGN-2: Улучшить карточки проектов
**Файл:** `docs/index.html` + `docs/static/css/style.css`  
**Фикс:** Добавить в каждую project-card:
- Теги технологий (несколько, не только язык)
- Кнопки: "Open Project Page" + "GitHub"
- hover: `transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,180,216,0.15)`
- Полное описание проекта (восстановить обрезанный текст)

### DESIGN-3: Переделать nav в горизонтальный topbar
**Файл:** `docs/index.html`  
**Проблема:** Вертикальный nav в правом углу — неудобен на мобильных.  
**Фикс:**
```css
nav {
  position: fixed; top: 0; left: 0; right: 0;
  display: flex; justify-content: space-between; align-items: center;
  padding: 0 40px; height: 64px;
  background: rgba(10, 14, 26, 0.9); backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  z-index: 1000; flex-direction: row; gap: 0;
}
/* Логотип слева */
.nav-logo { color: var(--primary-color); font-weight: 700; font-size: 1.1em; }
/* Ссылки справа */
.nav-links { display: flex; gap: 8px; flex-direction: row; background: none; border-radius: 0; }
```
Добавить `<span class="nav-logo">TC</span>` слева в nav.
Добавить `padding-top: 64px` к `.container`.

### DESIGN-4: Улучшить hero-секцию
**Файл:** `docs/index.html` — `<header>`  
**Фикс:**
- `min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center;`
- Добавить typewriter эффект для специализаций под subtitle
- Добавить stats-bar: "3 Projects | Open Source | Python & AI"

---

## 🟡 НОВЫЙ ФУНКЦИОНАЛ: СТРАНИЦЫ ПРОЕКТОВ

### PROJECTS-1: Создать отдельные HTML-страницы проектов
Создать 3 новых файла со структурой:
- `docs/project/jarvis/index.html`
- `docs/project/sorter/index.html`
- `docs/project/copytool/index.html`

**Шаблон страницы проекта:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[PROJECT NAME] — Totsamuychel</title>
  <link rel="stylesheet" href="/WebPortfolio/static/css/style.css">
</head>
<body>
  <!-- та же nav что на index.html -->
  <nav>...</nav>

  <main style="max-width: 900px; margin: 100px auto; padding: 0 24px;">
    <a href="/WebPortfolio/" style="color: var(--primary-color);">← Back to Portfolio</a>

    <section class="project-hero" style="margin: 40px 0;">
      <h1>[PROJECT NAME]</h1>
      <p class="subtitle">[TAGLINE]</p>
      <div style="display:flex; gap:12px; margin-top:20px;">
        <span class="skill-badge">Python</span>
        <a href="https://github.com/Totsamuychel/[REPO]" target="_blank" class="social-btn">View on GitHub →</a>
      </div>
    </section>

    <section class="glass-card" style="padding:40px; margin: 30px 0;">
      <h2>About the Project</h2>
      <p>[FULL DESCRIPTION]</p>
    </section>

    <section class="glass-card" style="padding:40px; margin: 30px 0;">
      <h2>Technologies Used</h2>
      <div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:16px;">[TECH BADGES]</div>
    </section>

    <section class="glass-card" style="padding:40px; margin: 30px 0;">
      <h2>Key Features</h2>
      <ul style="list-style:none; padding:0;">[FEATURES]</ul>
    </section>
  </main>

  <footer>...</footer>
  <script src="/WebPortfolio/static/js/script.js"></script>
</body>
</html>
```

### PROJECTS-2: Контент для каждой страницы

**Jarvis** (`docs/project/jarvis/`):
- Полное название: "Jarvis — Local AI Voice Assistant"
- Описание: Голосовой ассистент с Speech-to-Text, Computer Vision и управлением ПК. Работает локально без облака.
- Технологии: Python, OpenCV, SpeechRecognition, Ollama, PyAutoGUI, PIL
- Фичи: распознавание речи, анализ изображений с экрана, управление мышью/клавиатурой, локальные LLM-модели

**Google Account Sorter** (`docs/project/sorter/`):
- Полное название: "Google Account Sorter — Automated Sheet Management"
- Описание: Автоматическая сортировка данных в Google Sheets с поддержкой множества Google-аккаунтов
- Технологии: Python, Google Sheets API, OAuth2, gspread

**CopyTool App with AI** (`docs/project/copytool/`):
- Полное название: "CopyTool — AI Screen Text Detector"
- Описание: Использует локальную AI-модель для детекции выделенного текста на экране и копирования в буфер обмена
- Технологии: Python, Ollama, PIL/Pillow, PyAutoGUI, Local LLM

### PROJECTS-3: Обновить карточки на главной
**Файл:** `docs/index.html` — `.projects-grid`  
Убедиться что onclick-пути корректны:
- `/WebPortfolio/project/jarvis/`
- `/WebPortfolio/project/sorter/`
- `/WebPortfolio/project/copytool/`

---

## 🟢 УЛУЧШЕНИЯ КАЧЕСТВА

### QA-1: Meta теги SEO + Open Graph
**Файл:** `docs/index.html` — в `<head>`:
```html
<meta name="description" content="Totsamuychel — AI/ML Developer. Python, Local AI Models, Computer Vision, Open Source.">
<meta property="og:title" content="Totsamuychel — AI Developer Portfolio">
<meta property="og:description" content="AI/ML Developer specializing in local AI, computer vision and automation.">
<meta property="og:url" content="https://totsamuychel.github.io/WebPortfolio/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
```

### QA-2: Исправить lang атрибут
`<html lang="ru">` → `<html lang="en">`

### QA-3: Мобильная адаптация
```css
@media (max-width: 768px) {
  nav { padding: 0 16px; }
  nav .nav-links a span { display: none; } /* скрыть emoji в nav на мобиле */
  #about > div[style*="grid-template-columns"] { display: block !important; }
  .projects-grid { grid-template-columns: 1fr !important; }
  header { padding: 20px; }
}
```

### QA-4: SVG Favicon
```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%230077b6'/><text y='70' x='50' text-anchor='middle' font-size='55' font-family='sans-serif' font-weight='bold' fill='%2300b4d8'>TC</text></svg>">
```

---

## 📁 ИТОГОВАЯ СТРУКТУРА ФАЙЛОВ

```
docs/
├── index.html                    ← ОБНОВИТЬ
├── project/
│   ├── jarvis/index.html         ← СОЗДАТЬ
│   ├── sorter/index.html         ← СОЗДАТЬ
│   └── copytool/index.html       ← СОЗДАТЬ
├── static/
│   ├── css/style.css             ← ОБНОВИТЬ (палитра + nav + мобайл)
│   └── js/
│       ├── script.js             ← ПРОВЕРИТЬ (исправить битый путь)
│       ├── translations.js
│       ├── language-switcher.js
│       ├── themes.js
│       └── theme-switcher.js
└── blog/
```

---

## ✅ ЧЕКЛИСТ ДЛЯ АГЕНТА

- [ ] BUG-1: Убрать `<h4>Totsamuychel</h4>` из About карточки
- [ ] BUG-2: Заменить emoji-аватары testimonials на SVG-инициалы
- [ ] BUG-3: Исправить путь `/static/css/js/` → `/static/js/`
- [ ] BUG-4: Восстановить полные имена и тексты testimonials
- [ ] DESIGN-1: Заменить #667eea/#764ba2 на cyan/navy палитру
- [ ] DESIGN-2: Улучшить project-cards (теги, кнопки, hover)
- [ ] DESIGN-3: Nav → горизонтальный topbar с логотипом TC
- [ ] DESIGN-4: Hero: min-height 100vh + typewriter эффект
- [ ] PROJECTS-1/2/3: Создать 3 страницы проектов с контентом
- [ ] QA-1: Добавить meta/og теги
- [ ] QA-2: lang="ru" → lang="en"
- [ ] QA-3: Media queries для мобильных
- [ ] QA-4: SVG favicon

---

## 🔮 FUTURE (не делать сейчас)

1. Hugging Face Spaces iframe для AI-демо
2. Lottie анимации (lottie-web CDN) вместо статических иконок
3. Python-скрипт: GitHub API → auto-update projects из репозиториев
4. Blog секция с реальными статьями
5. Contact форма через Formspree

# 🤖 AI/ML Developer Portfolio — Totsamuychel

[![GitHub Pages](https://img.shields.io/badge/Live-Demo-00b4d8?style=for-the-badge&logo=github)](https://totsamuychel.github.io/WebPortfolio/)
[![Python](https://img.shields.io/badge/Python-3.10+-0077b6?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)

A modern, high-performance web portfolio designed for an AI/ML developer. This project showcases technical expertise in local AI models, computer vision, and automation through a sleek, "cyber-tech" interface.

## 🎯 Purpose
The primary goal of this portfolio is to provide a deep dive into my professional projects. Unlike standard landing pages, this site features:
- **Technical Deep Dives:** Detailed explanations of how my AI tools (like Jarvis and CopyTool) work under the hood.
- **Local AI Focus:** Highlighting the shift towards privacy-focused, local-first AI implementations.
- **Performance Metrics:** Real-world stats on speed and accuracy for ML models.

## 🚀 Key Features
- **Project Showcases:** Interactive cards with tech stacks, GitHub links, and dedicated detail pages.
- **Modern UI/UX:** 
  - **Glassmorphism:** Elegant semi-transparent cards with backdrop blur.
  - **Cyan/Teal Palette:** A professional, technological color scheme.
  - **Typewriter Effect:** Dynamic introduction in the Hero section.
  - **Fully Responsive:** Optimized for desktop, tablets, and mobile devices.
- **Technical Content:** Integrated blog section for AI research and automation guides.
- **SEO & Social Ready:** Complete Open Graph meta tags and SVG favicon for perfect social sharing.

## 🛠 Tech Stack
- **Backend/CMS:** [Django](https://www.djangoproject.com/) — Used for content management and rapid development.
- **Static Generation:** [django-distill](https://github.com/meeb/django-distill) — Transforms the dynamic Django site into high-performance static HTML for hosting.
- **Frontend:** Vanilla HTML5, CSS3 (Modern Flexbox/Grid), and JavaScript.
- **Database:** SQLite3 (Local development).
- **Deployment:** [GitHub Pages](https://pages.github.com/).

## 🏗 Architecture
This project uses a **hybrid workflow**:
1. **Manage Content:** Add projects, skills, and testimonials via the Django Admin interface.
2. **Generate Static:** Convert the entire site into a static structure in the `/docs` folder.
3. **Deploy:** Push the `/docs` folder to GitHub Pages for free, fast, and secure hosting without needing a live Python server.

## 📦 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Totsamuychel/WebPortfolio.git
   cd WebPortfolio
   ```

2. **Install dependencies:**
   ```bash
   pip install django django-distill
   ```

3. **Apply migrations and update data:**
   ```bash
   python manage.py migrate
   python update_db.py
   ```

4. **Run development server:**
   ```bash
   python manage.py runserver
   ```

## 🔄 How to Update the Live Site
To update the static files in the `/docs` folder after changing content in Django:
1. Run `python manage.py collectstatic --noinput`
2. Run `python manage.py distill-local ./docs --force`
3. Push changes to the `main` branch.

---
Created with passion for **AI & Automation** by [Totsamuychel](https://github.com/Totsamuychel).

// Language Switcher & UI Enhancements
document.addEventListener('DOMContentLoaded', function() {
    const currentLang = getCurrentLanguage();
    
    // Если язык не выбран, показываем модальное окно
    if (!localStorage.getItem('language')) {
        showLanguageModal();
    } else {
        applyLanguage(currentLang);
    }
    
    addLanguageSwitcher();
    initScrollEffects();
});

function showLanguageModal() {
    const modal = document.createElement('div');
    modal.id = 'language-modal';
    modal.style.cssText = `
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(10, 14, 26, 0.95); display: flex; align-items: center;
        justify-content: center; z-index: 10000; backdrop-filter: blur(20px);
        animation: fadeIn 0.5s ease;
    `;
    
    const content = document.createElement('div');
    content.className = 'glass-card';
    content.style.cssText = `
        padding: 60px; text-align: center; max-width: 500px;
        animation: slideUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 25px 80px rgba(0, 180, 216, 0.2);
    `;
    
    content.innerHTML = `
        <h2 style="font-size: 2.5em; margin-bottom: 20px;" class="text-gradient">
            ${t('selectLanguage', 'en')}
        </h2>
        <p style="color: var(--text-secondary); margin-bottom: 40px; font-size: 1.1em;">
            Choose your preferred language<br/>Виберіть вашу мову
        </p>
        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
            <button class="project-btn" data-lang="en">🇬🇧 English</button>
            <button class="project-btn secondary" data-lang="uk">🇺🇦 Українська</button>
        </div>
    `;
    
    modal.appendChild(content);
    document.body.appendChild(modal);
    
    modal.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', function() {
            setLanguage(this.dataset.lang);
        });
    });
}

function applyLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        const translation = t(key, lang);
        if (translation !== key) {
            el.textContent = translation;
        }
    });

    document.querySelectorAll('.category-name').forEach(el => {
        const cat = el.dataset.category;
        const keyMap = {
            "Языки программирования": "LANG",
            "ML/AI Фреймворки": "FRAMEWORK",
            "Инструменты & Библиотеки": "TOOL",
            "Базы данных": "DB",
            "DevOps/Инструменты": "DEVOPS",
            "Специализации": "SPEC"
        };
        const key = keyMap[cat] || cat;
        el.textContent = t(key, lang);
    });

    // Перевод названий проектов
    document.querySelectorAll('[data-project-title]').forEach(el => {
        const slug = el.dataset.projectTitle;
        const key = `project_${slug.replace(/-/g, '_')}_title`;
        const translation = t(key, lang);
        if (translation !== key) el.textContent = translation;
    });

    // Перевод описаний проектов
    document.querySelectorAll('[data-project-desc]').forEach(el => {
        const slug = el.dataset.projectDesc;
        const key = `project_${slug.replace(/-/g, '_')}_desc`;
        const translation = t(key, lang);
        if (translation !== key) el.textContent = translation;
    });

    document.title = `${t('title', lang)} - AI Developer Portfolio`;
}

function addLanguageSwitcher() {
    if (document.getElementById('language-switcher')) return;
    const currentLang = getCurrentLanguage();
    const btn = document.createElement('button');
    btn.id = 'language-switcher';
    btn.className = 'project-btn secondary';
    btn.style.cssText = `
        position: fixed; bottom: 30px; left: 30px; z-index: 999;
        padding: 10px 20px; border-radius: 50px; font-size: 0.9em;
        backdrop-filter: blur(10px);
    `;
    btn.textContent = currentLang === 'en' ? '🇺🇦 UK' : '🇬🇧 EN';
    btn.addEventListener('click', () => setLanguage(currentLang === 'en' ? 'uk' : 'en'));
    document.body.appendChild(btn);
}

function initScrollEffects() {
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('section, .glass-card, .project-card').forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });
}

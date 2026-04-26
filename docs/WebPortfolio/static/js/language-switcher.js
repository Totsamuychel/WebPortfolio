// Language Switcher
document.addEventListener('DOMContentLoaded', function() {
    // Небольшая задержка для полной загрузки DOM
    setTimeout(function() {
        const currentLang = getCurrentLanguage();
        
        // Если язык не выбран, показываем модальное окно
        if (!localStorage.getItem('language')) {
            showLanguageModal();
        } else {
            // Применяем язык к странице
            applyLanguage(currentLang);
        }
        
        // Добавляем кнопку переключения языка
        addLanguageSwitcher();
    }, 100);
});

function showLanguageModal() {
    const modal = document.createElement('div');
    modal.id = 'language-modal';
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        backdrop-filter: blur(10px);
        animation: fadeIn 0.5s ease;
    `;
    
    const content = document.createElement('div');
    content.style.cssText = `
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        border: 2px solid rgba(102, 126, 234, 0.5);
        border-radius: 30px;
        padding: 60px 40px;
        text-align: center;
        max-width: 500px;
        animation: slideUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 25px 80px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    `;
    
    // Добавляем фоновый эффект
    content.innerHTML = `
        <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%); animation: rotate 20s linear infinite;"></div>
        
        <div style="position: relative; z-index: 1;">
            <h2 style="
                font-size: 2.5em;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 20px;
                color: #fff;
                font-weight: 700;
            ">
                ${t('selectLanguage', 'en')}
            </h2>
            
            <p style="
                color: #a0a0a0;
                font-size: 1.1em;
                margin-bottom: 40px;
                line-height: 1.6;
            ">
                Choose your preferred language<br/>Виберіть вашу мову
            </p>
            
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <button class="lang-btn" data-lang="en" style="
                    padding: 15px 40px;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    border: none;
                    border-radius: 25px;
                    font-size: 1.1em;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                ">
                    🇬🇧 ${t('english', 'en')}
                </button>
                
                <button class="lang-btn" data-lang="uk" style="
                    padding: 15px 40px;
                    background: rgba(102, 126, 234, 0.2);
                    color: #667eea;
                    border: 2px solid #667eea;
                    border-radius: 25px;
                    font-size: 1.1em;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                ">
                    🇺🇦 ${t('ukrainian', 'en')}
                </button>
            </div>
        </div>
    `;
    
    modal.appendChild(content);
    document.body.appendChild(modal);
    
    // Обработчики кнопок
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const lang = this.dataset.lang;
            // Добавляем анимацию перед переходом
            modal.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => {
                setLanguage(lang);
            }, 300);
        });
        
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
            this.style.boxShadow = '0 20px 50px rgba(102, 126, 234, 0.5)';
        });
        
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 10px 30px rgba(102, 126, 234, 0.3)';
        });
    });
}

function applyLanguage(lang) {
    // Обновляем все элементы с data-i18n атрибутом
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.dataset.i18n;
        element.textContent = t(key, lang);
    });
    
    // Обновляем атрибуты placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.dataset.i18nPlaceholder;
        element.placeholder = t(key, lang);
    });
    
    // Обновляем категории навыков
    document.querySelectorAll('.category-name').forEach(element => {
        const category = element.dataset.category;
        // Преобразуем русское название в код категории
        let categoryCode = category;
        if (category === "Языки программирования") categoryCode = "LANG";
        else if (category === "ML/AI Фреймворки") categoryCode = "FRAMEWORK";
        else if (category === "Инструменты & Библиотеки") categoryCode = "TOOL";
        else if (category === "Базы данных") categoryCode = "DB";
        else if (category === "DevOps/Инструменты") categoryCode = "DEVOPS";
        else if (category === "Специализации") categoryCode = "SPEC";
        
        element.textContent = t(categoryCode, lang);
    });
    
    // Обновляем title страницы
    document.title = `${t('title', lang)} - AI Developer Portfolio`;
}

function addLanguageSwitcher() {
    // Проверяем, не добавлена ли уже кнопка
    if (document.getElementById('language-switcher')) return;
    
    const currentLang = getCurrentLanguage();
    const switcherBtn = document.createElement('button');
    switcherBtn.id = 'language-switcher';
    switcherBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        left: 20px;
        padding: 10px 18px;
        background: rgba(102, 126, 234, 0.2);
        border: 1px solid #667eea;
        border-radius: 20px;
        color: #667eea;
        cursor: pointer;
        font-size: 0.9em;
        font-weight: 600;
        transition: all 0.3s ease;
        z-index: 999;
    `;
    
    switcherBtn.textContent = currentLang === 'en' ? '🇺🇦 Українська' : '🇬🇧 English';
    
    switcherBtn.addEventListener('mouseenter', function() {
        this.style.background = 'rgba(102, 126, 234, 0.3)';
        this.style.transform = 'scale(1.05)';
    });
    
    switcherBtn.addEventListener('mouseleave', function() {
        this.style.background = 'rgba(102, 126, 234, 0.2)';
        this.style.transform = 'scale(1)';
    });
    
    switcherBtn.addEventListener('click', function() {
        const newLang = currentLang === 'en' ? 'uk' : 'en';
        setLanguage(newLang);
    });
    
    document.body.appendChild(switcherBtn);
}

// Добавляем стили для анимаций
const style = document.createElement('style');
style.textContent = `
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
`;
document.head.appendChild(style);

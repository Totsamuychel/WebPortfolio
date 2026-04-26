// Theme System
const themes = {
    dark: {
        name: 'Dark',
        icon: '🌙',
        colors: {
            bg: 'linear-gradient(135deg, #0f0c29, #302b63, #24243e)',
            primary: '#667eea',
            secondary: '#764ba2',
            text: '#e0e0e0',
            textSecondary: '#a0a0a0',
            cardBg: 'rgba(255, 255, 255, 0.05)',
            cardBorder: 'rgba(255, 255, 255, 0.1)',
            navBg: 'rgba(0, 0, 0, 0.8)',
        }
    },
    light: {
        name: 'Light',
        icon: '☀️',
        colors: {
            bg: 'linear-gradient(135deg, #f5f7fa, #c3cfe2)',
            primary: '#5a67d8',
            secondary: '#6b46c1',
            text: '#1a202c',
            textSecondary: '#4a5568',
            cardBg: 'rgba(255, 255, 255, 0.9)',
            cardBorder: 'rgba(90, 103, 216, 0.2)',
            navBg: 'rgba(255, 255, 255, 0.95)',
        }
    },
    purple: {
        name: 'Purple',
        icon: '💜',
        colors: {
            bg: 'linear-gradient(135deg, #1a0033, #330066, #4d0099)',
            primary: '#b366ff',
            secondary: '#ff66ff',
            text: '#f0e6ff',
            textSecondary: '#d9b3ff',
            cardBg: 'rgba(255, 255, 255, 0.08)',
            cardBorder: 'rgba(179, 102, 255, 0.3)',
            navBg: 'rgba(26, 0, 51, 0.9)',
        }
    }
};

// Получить текущую тему
function getCurrentTheme() {
    return localStorage.getItem('theme') || 'dark';
}

// Установить тему
function setTheme(themeName) {
    if (!themes[themeName]) return;
    
    localStorage.setItem('theme', themeName);
    applyTheme(themeName);
}

// Применить тему
function applyTheme(themeName) {
    const theme = themes[themeName];
    if (!theme) return;
    
    const root = document.documentElement;
    const colors = theme.colors;
    
    // Устанавливаем CSS переменные
    root.style.setProperty('--bg-gradient', colors.bg);
    root.style.setProperty('--primary-color', colors.primary);
    root.style.setProperty('--secondary-color', colors.secondary);
    root.style.setProperty('--text-color', colors.text);
    root.style.setProperty('--text-secondary', colors.textSecondary);
    root.style.setProperty('--card-bg', colors.cardBg);
    root.style.setProperty('--card-border', colors.cardBorder);
    root.style.setProperty('--nav-bg', colors.navBg);
    
    // Применяем стили к body
    document.body.style.background = colors.bg;
    document.body.style.color = colors.text;
    
    // Обновляем все элементы с классами
    updateThemeElements(themeName);
    
    // Добавляем класс темы к body
    document.body.className = document.body.className.replace(/theme-\w+/g, '');
    document.body.classList.add(`theme-${themeName}`);
}

// Обновить элементы при смене темы
function updateThemeElements(themeName) {
    const theme = themes[themeName];
    const colors = theme.colors;
    
    // Обновляем навигацию
    const nav = document.querySelector('nav');
    if (nav) {
        nav.style.background = colors.navBg;
        nav.style.borderColor = colors.cardBorder;
    }
    
    // Обновляем карточки проектов
    document.querySelectorAll('.project-card').forEach(card => {
        card.style.background = colors.cardBg;
        card.style.borderColor = colors.cardBorder;
        card.style.color = colors.text;
    });
    
    // Обновляем карточки навыков
    document.querySelectorAll('.skill-category').forEach(card => {
        card.style.background = colors.cardBg;
        card.style.borderColor = colors.cardBorder;
        card.style.color = colors.text;
    });
    
    // Обновляем карточки отзывов
    document.querySelectorAll('.testimonial-card').forEach(card => {
        card.style.background = colors.cardBg;
        card.style.borderColor = colors.cardBorder;
        card.style.color = colors.text;
    });
    
    // Обновляем карточки блога
    document.querySelectorAll('.blog-card').forEach(card => {
        card.style.background = colors.cardBg;
        card.style.borderColor = colors.cardBorder;
        card.style.color = colors.text;
    });
    
    // Обновляем заголовки
    document.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(heading => {
        heading.style.color = colors.text;
    });
    
    // Обновляем ссылки
    document.querySelectorAll('a').forEach(link => {
        link.style.color = colors.primary;
    });
}

// Переключить на следующую тему
function toggleTheme() {
    const themeNames = Object.keys(themes);
    const currentTheme = getCurrentTheme();
    const currentIndex = themeNames.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themeNames.length;
    const nextTheme = themeNames[nextIndex];
    
    setTheme(nextTheme);
    updateThemeSwitcher();
}

// Инициализация при загрузке
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const currentTheme = getCurrentTheme();
        applyTheme(currentTheme);
        addThemeSwitcher();
    }, 50);
});

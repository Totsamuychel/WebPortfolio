// Theme Switcher UI
function addThemeSwitcher() {
    // Проверяем, не добавлен ли уже переключатель
    if (document.getElementById('theme-switcher')) return;
    
    const currentTheme = getCurrentTheme();
    const themeNames = Object.keys(themes);
    
    // Создаем контейнер для переключателя
    const container = document.createElement('div');
    container.id = 'theme-switcher-container';
    container.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 998;
        display: flex;
        gap: 10px;
        align-items: center;
        background: rgba(0, 0, 0, 0.3);
        padding: 10px 15px;
        border-radius: 30px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
        animation: slideInRight 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    `;
    
    // Создаем кнопки для каждой темы
    themeNames.forEach((themeName, index) => {
        const theme = themes[themeName];
        const btn = document.createElement('button');
        btn.id = `theme-btn-${themeName}`;
        btn.className = 'theme-btn';
        btn.dataset.theme = themeName;
        btn.title = `Switch to ${theme.name} theme`;
        
        const isActive = themeName === currentTheme;
        
        btn.style.cssText = `
            background: ${isActive ? 'rgba(102, 126, 234, 0.3)' : 'rgba(102, 126, 234, 0.1)'};
            border: ${isActive ? '2px solid #667eea' : '1px solid rgba(102, 126, 234, 0.2)'};
            color: #667eea;
            padding: 8px 12px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 1.2em;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            min-width: 40px;
            height: 40px;
        `;
        
        btn.textContent = theme.icon;
        
        btn.addEventListener('click', function() {
            setTheme(themeName);
            updateThemeSwitcher();
            
            // Добавляем анимацию
            this.style.animation = 'pulse 0.5s ease';
            setTimeout(() => {
                this.style.animation = '';
            }, 500);
        });
        
        btn.addEventListener('mouseenter', function() {
            if (themeName !== currentTheme) {
                this.style.background = 'rgba(102, 126, 234, 0.2)';
                this.style.transform = 'scale(1.1)';
            }
        });
        
        btn.addEventListener('mouseleave', function() {
            if (themeName !== currentTheme) {
                this.style.background = 'rgba(102, 126, 234, 0.1)';
                this.style.transform = 'scale(1)';
            }
        });
        
        container.appendChild(btn);
    });
    
    document.body.appendChild(container);
}

// Обновить переключатель тем
function updateThemeSwitcher() {
    const currentTheme = getCurrentTheme();
    const themeNames = Object.keys(themes);
    
    themeNames.forEach(themeName => {
        const btn = document.getElementById(`theme-btn-${themeName}`);
        if (!btn) return;
        
        const isActive = themeName === currentTheme;
        
        if (isActive) {
            btn.style.background = 'rgba(102, 126, 234, 0.3)';
            btn.style.border = '2px solid #667eea';
            btn.style.transform = 'scale(1.1)';
        } else {
            btn.style.background = 'rgba(102, 126, 234, 0.1)';
            btn.style.border = '1px solid rgba(102, 126, 234, 0.2)';
            btn.style.transform = 'scale(1)';
        }
    });
}

// Добавляем стили для анимаций
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.15);
        }
    }
    
    .theme-btn {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .theme-btn:active {
        transform: scale(0.95) !important;
    }
`;
document.head.appendChild(styleSheet);

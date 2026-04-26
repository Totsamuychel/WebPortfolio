// Core Visual Effects
document.addEventListener('DOMContentLoaded', () => {
    initStars();
    initParticles();
    initTypewriter();
});

function initStars() {
    const container = document.getElementById('stars');
    if (!container) return;
    
    for (let i = 0; i < 150; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        const size = Math.random() * 2 + 1;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 5}s`;
        star.style.animationDuration = `${Math.random() * 3 + 2}s`;
        container.appendChild(star);
    }
}

function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;
    
    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.width = '4px';
        particle.style.height = '4px';
        particle.style.background = 'var(--primary-color)';
        particle.style.borderRadius = '50%';
        particle.style.position = 'absolute';
        particle.style.opacity = '0.3';
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.animation = `float ${Math.random() * 10 + 10}s linear infinite`;
        container.appendChild(particle);
    }
}

function initTypewriter() {
    const el = document.getElementById('typewriter');
    if (!el) return;
    
    const currentLang = localStorage.getItem('language') || 'en';
    const text = currentLang === 'uk' 
        ? "AI & Machine Learning Розробник" 
        : "AI & Machine Learning Developer";
    
    let i = 0;
    el.textContent = '';
    function type() {
        if (i < text.length) {
            el.textContent += text.charAt(i);
            i++;
            setTimeout(type, 70);
        }
    }
    setTimeout(type, 800);
}

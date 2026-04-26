Fix two visual bugs in docs/index.html and docs/static/css/style.css:

---

## BUG 1: Doubled emoji icons in Skills section cards

**Problem:** Each skill category card has TWO emoji icons rendered side by side
(e.g. "💻 💻 Programming Languages", "🤖 🤖 ML/AI Frameworks").
This happens because the emoji character appears TWICE in the HTML —
once as a raw emoji inside <span> and once rendered by the browser's emoji font.

**Fix in docs/index.html:**
Find all <h3> inside .skill-category cards. Each looks like:
```html
<h3 ...>
  <span>
    💻
    
  </span> 
  <span class="category-name">...</span>
</h3>
```
The <span> containing the emoji has an extra blank line/whitespace after the emoji.
This causes the emoji to render twice on some systems.

Replace ALL skill category icon spans with a clean single-line version:
```html
<span class="skill-icon">💻</span>
```
And ensure each icon appears only once. Apply to all 6 skill cards:
- Programming Languages → 💻
- ML/AI Frameworks → 🤖
- Tools & Libraries → 📚
- Databases → 🗄️
- DevOps/Tools → ⚙️
- Specializations → 🎯

**Fix in docs/static/css/style.css:**
Add this rule to prevent emoji duplication via CSS:
```css
.skill-category h3 .skill-icon {
  font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
  font-size: 1.3em;
  line-height: 1;
  display: inline-block;
  width: 1.5em;
  text-align: center;
}
```

---

## BUG 2: Nav bar layout — fix to proper horizontal topbar

**Problem:** The nav is positioned as `position: fixed; top: 20px; right: 20px`
with `flex-direction: column` — it appears as a vertical pill in the top-right corner.
The current look (from screenshot) shows it centered horizontally but still looks off.

**Fix in docs/index.html:**
Replace the entire inline style on the <nav> element with a class:
```html
<nav class="main-nav">
  <span class="nav-logo">TC</span>
  <div class="nav-links">
    <a href="#about" onclick="scrollToSection('about')" data-i18n="about">👋 About</a>
    <a href="#skills" onclick="scrollToSection('skills')" data-i18n="skills">🛠️ Skills</a>
    <a href="#testimonials" onclick="scrollToSection('testimonials')" data-i18n="testimonials">💬 Testimonials</a>
    <a href="#projects" onclick="scrollToSection('projects')" data-i18n="projects">🚀 Projects</a>
  </div>
</nav>
```

**Fix in docs/static/css/style.css:**
Add this CSS (remove any old nav inline styles):
```css
.main-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  background: rgba(10, 14, 30, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(102, 126, 234, 0.25);
  z-index: 1000;
  gap: 0;
  border-radius: 0;
}

.nav-logo {
  color: #667eea;
  font-size: 1.2em;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-decoration: none;
  flex-shrink: 0;
}

.nav-links {
  display: flex;
  flex-direction: row;
  gap: 4px;
  align-items: center;
}

.nav-links a {
  color: #667eea;
  text-decoration: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.88em;
  white-space: nowrap;
  transition: background 0.2s, color 0.2s;
}

.nav-links a:hover {
  background: rgba(102, 126, 234, 0.15);
  color: #fff;
}

/* Push page content below fixed nav */
.container {
  padding-top: 72px;
}

@media (max-width: 768px) {
  .main-nav { padding: 0 16px; }
  .nav-logo { display: none; }
  .nav-links a { padding: 6px 10px; font-size: 0.8em; }
}
```

---

After making changes:
1. Save both files
2. Verify in browser that nav shows as a single horizontal bar at the top
3. Verify each skill card header has exactly ONE emoji icon
4. Do NOT change any other section
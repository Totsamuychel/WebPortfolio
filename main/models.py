from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('LANG', 'Языки программирования'),
        ('FRAMEWORK', 'ML/AI Фреймворки'),
        ('TOOL', 'Инструменты & Библиотеки'),
        ('DB', 'Базы данных'),
        ('DEVOPS', 'DevOps/Инструменты'),
        ('SPEC', 'Специализации'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=20, default="#667eea", help_text="HEX цвет или название класса")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-адрес проекта (например: jarvis)")
    short_description = models.CharField(max_length=300, help_text="Для карточки на главной")
    full_description = models.TextField(help_text="Полное описание для страницы проекта")
    how_it_works = models.TextField(blank=True, help_text="Подробное объяснение принципа работы проекта")
    features_list = models.TextField(blank=True, help_text="Список возможностей (каждая с новой строки)")
    code_snippet = models.TextField(blank=True, help_text="Пример ключевого кода для демонстрации")
    technologies = models.ManyToManyField(Skill, related_name='projects')
    github_link = models.URLField(blank=True)
    
    # Для красивых метрик на странице проекта
    metric_speed = models.CharField(max_length=50, blank=True, help_text="Например: <200ms")
    metric_accuracy = models.CharField(max_length=50, blank=True, help_text="Например: 95%")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def get_features(self):
        return [f.strip() for f in self.features_list.split('\n') if f.strip()]

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    text = models.TextField()
    emoji = models.CharField(max_length=10, default="👨‍💻")

    def __str__(self):
        return self.author

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField() # В реальности лучше использовать RichTextField
    read_time = models.IntegerField(help_text="Время чтения в минутах")
    date = models.DateField()
    category_tag = models.CharField(max_length=50)

    def __str__(self):
        return self.title
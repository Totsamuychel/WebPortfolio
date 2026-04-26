from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Testimonial, BlogPost

def get_all_projects():
    for project in Project.objects.all():
        yield {'slug': project.slug}

def get_all_posts():
    for post in BlogPost.objects.all():
        yield {'slug': post.slug}

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    testimonials = Testimonial.objects.all()
    posts = BlogPost.objects.all().order_by('-date')
    
    # Группируем навыки по категориям для вывода
    skills_dict = {}
    for cat_code, cat_name in Skill.CATEGORY_CHOICES:
        skills_dict[cat_name] = Skill.objects.filter(category=cat_code)

    context = {
        'projects': projects,
        'testimonials': testimonials,
        'posts': posts,
        'skills_dict': skills_dict,
    }
    return render(request, 'home.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})
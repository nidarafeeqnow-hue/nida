from django.shortcuts import render

def home(request):
    projects = [
        {
            'title': 'Personal Portfolio',
            'description': 'A clean Django portfolio website with responsive sections and smooth navigation.',
            'tech': 'Django, HTML, CSS, JavaScript',
        },
        {
            'title': 'Task Dashboard',
            'description': 'A compact interface concept for tracking tasks, deadlines, and daily priorities.',
            'tech': 'Python, SQLite, UI Design',
        },
        {
            'title': 'Landing Page',
            'description': 'A fast, mobile-friendly page layout for a small business or personal brand.',
            'tech': 'HTML, CSS, JavaScript',
        },
    ]

    skills = ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'SQLite', 'Git']

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'skills': skills,
    })

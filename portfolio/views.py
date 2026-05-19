from django.shortcuts import render


def home(request):
    projects = [
        {
            "title": "Portfolio Website",
            "description": "A clean personal website built with Django, HTML, CSS, and JavaScript.",
            "tools": "Django, HTML, CSS, JavaScript",
        },
        {
            "title": "Task Dashboard",
            "description": "A simple dashboard concept for organizing daily work and project notes.",
            "tools": "Python, SQLite, Bootstrap",
        },
        {
            "title": "Weather App",
            "description": "A local-first interface that displays weather information in a readable layout.",
            "tools": "JavaScript, API, CSS",
        },
    ]

    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "Git"]

    return render(
        request,
        "portfolio/home.html",
        {
            "name": "Your Name",
            "role": "Python Django Developer",
            "projects": projects,
            "skills": skills,
        },
    )

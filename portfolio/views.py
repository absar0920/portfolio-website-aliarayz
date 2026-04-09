from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Skill, Project, Experience, Achievement, Education, Automation, ContactMessage

def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    achievements = Achievement.objects.all()
    education = Education.objects.all()
    automations = Automation.objects.all()

    # Filter projects that have a video file
    video_projects = [p for p in projects if p.video_file]

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'video_projects': video_projects,
        'video_projects_preview': video_projects[:4],
        'show_all_videos_btn': len(video_projects) > 4,
        'show_all_projects_btn': projects.count() > 6,
        'experiences': experiences,
        'achievements': achievements,
        'education': education,
        'automations': automations,
    }
    return render(request, 'portfolio/index.html', context)


def all_videos(request):
    """Display all project demonstration videos."""
    profile = Profile.objects.first()
    projects = Project.objects.all()
    video_projects = [p for p in projects if p.video_file]

    context = {
        'profile': profile,
        'video_projects': video_projects,
    }
    return render(request, 'portfolio/all_videos.html', context)


def all_projects(request):
    """Display all featured projects with full details."""
    profile = Profile.objects.first()
    projects = Project.objects.all()

    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'portfolio/all_projects.html', context)


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send Email Notification
        try:
            full_message = f"Message from: {name} ({email})\n\nSubject: {subject}\n\nMessage:\n{message}"
            send_mail(
                subject=f"New Portfolio Contact: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            # Log the error but don't fail the request completely if DB save worked
            print(f"SMTP Error: {e}")
            
        return JsonResponse({'status': 'success', 'message': 'Thank you! Your message has been sent and I will get back to you soon.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

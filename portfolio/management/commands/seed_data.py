import os
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience, Achievement, Education, Automation

class Command(BaseCommand):
    help = 'Seeds the database with data from portfolio.md'

    def handle(self, *args, **options):
        # Clear existing data
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Achievement.objects.all().delete()
        Education.objects.all().delete()
        Automation.objects.all().delete()

        # 1. Profile
        Profile.objects.create(
            name="Arayz Wasti",
            title="Experienced Backend Developer | Python, Django, REST APIs & FastAPI",
            about="I'm Arayz Wasti, a passionate and results-driven Python Backend Developer with over 4 years of personal development experience and 2.5+ years of professional experience at Enigmatix. I specialize in building fast, secure, and scalable backend systems and RESTful APIs.",
            email="arayzwasti111@gmail.com",
            github="https://github.com/Arayz-Wasti",
            linkedin="https://www.linkedin.com/in/aliarayz/"
        )

        # 2. Skills
        skills_data = [
            ('Backend', 'Python', 'fab fa-python'),
            ('Backend', 'Django & DRF', 'fas fa-server'),
            ('Backend', 'FastAPI', 'fas fa-bolt'),
            ('Backend', 'Flask', 'fas fa-flask'),
            ('Databases', 'PostgreSQL', 'fas fa-database'),
            ('Databases', 'MySQL', 'fas fa-database'),
            ('Databases', 'MongoDB', 'fas fa-file-code'),
            ('DevOps', 'Docker & Podman', 'fab fa-docker'),
            ('DevOps', 'Linux Deployment', 'fab fa-linux'),
            ('Data', 'Scrapy', 'fas fa-spider'),
            ('Data', 'BeautifulSoup', 'fas fa-broom'),
            ('ML', 'NumPy & Pandas', 'fas fa-chart-line'),
            ('Frontend', 'HTML5 & CSS3', 'fab fa-html5'),
            ('Frontend', 'JavaScript', 'fab fa-js'),
        ]
        for cat, name, icon in skills_data:
            Skill.objects.create(category=cat, name=name, icon_class=icon)

        # 3. Projects
        # 3. Projects
        projects = [
            {
                'title': 'Crypto Market Intelligence System',
                'desc': 'Real-time crypto data processing and market sentiment classification.',
                'tech': 'Python, API Integration, JSON Processing',
                'bullets': 'Real-time crypto data processing\nMarket sentiment classification\nStructured JSON output engine\nOptimized calculation accuracy',
            },
            {
                'title': 'VIN Report Management System',
                'desc': 'Django-based admin dashboard with REST API architecture for secure report management.',
                'tech': 'Django, REST API, PostgreSQL',
                'bullets': 'Django-based admin dashboard\nREST API architecture\nSecure payment and request workflow\nScalable backend design',
            },
            {
                'title': 'Enterprise Data Automation Tool',
                'desc': 'Scrapy-based scraping engine and automated processing pipelines for enterprise data.',
                'tech': 'Scrapy, BeautifulSoup, PostgreSQL, Python',
                'bullets': 'Scrapy-based scraping engine\nAutomated processing pipelines\nPostgreSQL data storage\nPerformance-optimized queries',
            },
            {
                'title': 'E-commerce Platform',
                'desc': 'Full-featured e-commerce solution with multi-payment gateway integration.',
                'tech': 'Django, Stripe, PayPal, Razorpay',
                'bullets': 'Customized Django-based admin dashboard\nCheckout workflow, add to cart, wishlist, order management etc\nREST API architecture\nSecure payment and request workflow(Stripe, PayPal, Razorpay)\nScalable backend design',
            },
            {
                'title': 'Attendance Management System',
                'desc': 'Comprehensive system with Face Recognition (OpenCV) and background processing.',
                'tech': 'Django, Redis, Celery, OpenCV, Face Recognition',
                'bullets': 'Django-based admin dashboard\nREST API architecture\nAttendance tracking and management\nScalable backend design\nimplemented the SMTP for email notifications\nStripe for fine payment\nImplemented the JWT authentication\nImplemented the Celery for background tasks\nImplemented the Redis for caching\nImplemented Face Recognition for attendance marking(OpenCV, face_recognition, dlib)',
            },
            {
                'title': 'Zain Iraq Features Integration',
                'desc': 'Integration of multiple features and third-party APIs for the Zain Iraq application.',
                'tech': 'Python, aiohttp, Redis, RabbitMQ, PostgreSQL, Remedy API',
                'bullets': 'Implemented the aiohttp_client_session for timeout handling\nImplemented the Redis for caching\nImplemented the submit and track complaint feature in zain iraq app.(Integrating third party remedy Api)\nImplemented the ZainFi devices feature in zain iraq app.\nImplemented the 4G booster Api integration in zain iraq app.\nImplemented the new kafoo offer feature in zain iraq app.\nImplemented the SHARING BUNDLE integration in zain iraq app.(Integrating third party rsc relation Api)\nImplemented PostgreSQL and successfully migrated all DMart custom databases to PostgreSQL. Managed a multi-database architecture using both PostgreSQL and dmart database..\nImplemented the rabbit mq worker for backend task processing.',
            }
        ]
        for i, p in enumerate(projects):
            # Use specific video for VIN project if it exists
            video_file = 'videos/video.mp4'
            if p['title'] == 'N8n Filtering orders':
                video_file = 'videos/filtering-orders-n8n.mp4'
            
            Project.objects.create(
                title=p['title'],
                description=p['desc'],
                tech_stack=p['tech'],
                bullet_points=p['bullets'],
                video_file=video_file,
                order=i
            )

        # 4. Experience
        Experience.objects.create(
            company="Enigmatix",
            role="Backend Developer",
            start_date="2.5+ Years",
            description="Develop scalable backend systems using Django, Flask, and FastAPI\nDesign and implement high-performance REST APIs\nOptimize database performance and query efficiency\nEnsure security, testing, and production stability",
            order=1
        )

        # 5. Education
        Education.objects.create(
            degree="Bachelor of Science in Information Technology",
            institution="Islamia University of Bahawalpur",
            location="Bahawalpur, Pakistan",
            date_range="2022-2026"
        )

        # 6. Automations
        automations = [
            ('Background Tasks', 'Celery + RabbitMQ for async processing', 'fas fa-tasks'),
            ('Caching', 'Redis to speed up responses and reduce DB load', 'fas fa-memory'),
            ('Authentication', 'JWT token-based secure authentication', 'fas fa-lock'),
            ('Face Recognition', 'OpenCV + dlib for automated marking', 'fas fa-user-check'),
        ]
        for title, desc, icon in automations:
            Automation.objects.create(title=title, description=desc, icon=icon)

        self.stdout.write(self.style.SUCCESS('Successfully seeded portfolio data'))

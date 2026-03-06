import json
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Message, Article, Statistics, Education, Experience, Skill


@require_http_methods(["GET"])
def health(request):
    """Health check endpoint"""
    return JsonResponse({"ok": True})


@require_http_methods(["GET"])
def statistics(request):
    """Get portfolio statistics"""
    try:
        stats = Statistics.get_instance()
        return JsonResponse({
            "years_experience": stats.years_experience,
            "happy_clients": stats.happy_clients,
            "projects_done": stats.projects_done,
            "downloads": stats.downloads,
            "updated_at": stats.updated_at.isoformat()
        })
    except Exception as e:
        print(f"Error fetching statistics: {e}")
        return JsonResponse(
            {"error": "Impossible de récupérer les statistiques."},
            status=500
        )


@require_http_methods(["GET"])
def resume(request):
    """Get resume data (education, experience, skills)"""
    try:
        education = list(Education.objects.all().values(
            'id', 'title', 'school', 'description', 'time'
        ))
        experience = list(Experience.objects.all().values(
            'id', 'title', 'description', 'time'
        ))
        skills = list(Skill.objects.all().values(
            'id', 'name', 'percentage'
        ))

        return JsonResponse({
            "education": education,
            "experience": experience,
            "skills": skills
        })
    except Exception as e:
        print(f"Error fetching resume: {e}")
        return JsonResponse(
            {"error": "Impossible de récupérer le CV."},
            status=500
        )


@csrf_exempt
@require_http_methods(["POST"])
def contact(request):
    """Handle contact form submission"""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject', '')
    message = data.get('message')

    # Validate required fields
    if not name or not email or not message:
        return JsonResponse(
            {"error": "Les champs name, email et message sont requis."},
            status=400
        )

    try:
        # Save message to database
        Message.objects.create(
            name=name,
            email=email,
            subject=subject or None,
            message=message
        )

        # Send email if SMTP is configured
        if (os.getenv('SMTP_HOST') and os.getenv('SMTP_USER') and
            os.getenv('SMTP_PASS')):
            try:
                recipient = os.getenv('CONTACT_RECEIVER', 'Bdby0706@gmail.com')
                mail_subject = f"Nouveau message portfolio: {subject or 'Sans sujet'}"
                mail_message = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
                send_mail(
                    mail_subject,
                    mail_message,
                    os.getenv('SMTP_FROM', os.getenv('SMTP_USER')),
                    [recipient],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't fail the response
                print(f"Failed to send email: {e}")

        return JsonResponse({"ok": True})

    except Exception as e:
        print(f"Error in contact endpoint: {e}")
        return JsonResponse(
            {"error": "Erreur serveur lors de la sauvegarde."},
            status=500
        )


@require_http_methods(["GET"])
def articles_list(request):
    """Get all articles"""
    try:
        articles = Article.objects.all().values(
            'id', 'title', 'date', 'author', 'excerpt', 'content', 'cover', 'slug'
        )
        return JsonResponse(list(articles), safe=False)
    except Exception as e:
        print(f"Error fetching articles: {e}")
        return JsonResponse(
            {"error": "Impossible de lire les articles."},
            status=500
        )


@require_http_methods(["GET"])
def article_detail(request, slug):
    """Get a single article by slug or id"""
    try:
        # Try to find by slug first, then by id
        article = Article.objects.filter(slug=slug) | Article.objects.filter(id=slug)
        article = article.values(
            'id', 'title', 'date', 'author', 'excerpt', 'content', 'cover', 'slug'
        ).first()

        if not article:
            return JsonResponse(
                {"error": "Article introuvable"},
                status=404
            )

        return JsonResponse(article)

    except Exception as e:
        print(f"Error fetching article: {e}")
        return JsonResponse(
            {"error": "Erreur serveur lors de la lecture de l'article."},
            status=500
        )

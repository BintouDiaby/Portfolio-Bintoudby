#!/usr/bin/env python
"""
Populate the database with initial data
Usage: python populate.py
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Article, Message, Statistics, Education, Experience, Skill
from datetime import datetime

def populate_articles():
    """Populate articles"""
    articles_data = [
        {
            'id': 'apprendre-django-premier-projet',
            'title': 'Apprendre Django : premier projet backend',
            'date': '2025-01-15',
            'author': 'Diaby Nabintou',
            'excerpt': 'Guide pas-à-pas pour créer une API REST robuste avec Django et DRF.',
            'content': '<p>Ce guide accompagne le développeur dans la création d\'une API REST professionnelle en utilisant <strong>Django</strong> et <strong>Django REST Framework</strong>. Nous couvrons :</p>\n<ul>\n<li>Configuration de l\'environnement et bonnes pratiques de structure de projet</li>\n<li>Conception des modèles et relations (constraints, migrations)</li>\n<li>Serializers et validation côté serveur</li>\n<li>Création d\'API views, permissions et pagination</li>\n<li>Tests automatisés unitaires et d\'intégration</li>\n<li>Conseils de déploiement (Gunicorn, Nginx, variables d\'environnement)</li>\n</ul>\n<p>Exemple concret : un gestionnaire de notes pour une formation, avec modèles `Student`, `Course`, `Grade` et endpoints sécurisés. Nous incluons des extraits de code, exemples de tests et recommandations pour la mise en production.</p>',
            'cover': '/assets/images/article-django.jpg',
            'slug': 'apprendre-django-premier-projet'
        },
        {
            'id': 'interface-accessible-figma',
            'title': 'Concevoir une interface accessible avec Figma',
            'date': '2025-03-10',
            'author': 'Diaby Nabintou',
            'excerpt': 'Méthodes concrètes pour produire des maquettes accessibles et testables avec Figma.',
            'content': '<p>L\'accessibilité doit être pensée dès la phase de design. Cet article présente des workflows Figma pour :</p>\n<ul>\n<li>Structurer correctement l\'information et utiliser des composants réutilisables</li>\n<li>Vérifier les contrastes de couleur et tester avec des simulateurs</li>\n<li>Définir les points de focus et les états d\'interaction</li>\n<li>Préparer des specs et assets destinés aux développeurs (naming, tokens, export SVG)</li>\n</ul>\n<p>Nous proposons également une checklist de contrôle qualité et une courte démonstration de plugins Figma utiles pour l\'accessibility testing et l\'export des tokens.</p>',
            'cover': '/assets/images/article-figma.jpg',
            'slug': 'interface-accessible-figma'
        },
        {
            'id': 'flutter-todo-app',
            'title': 'Créer une application mobile simple avec Flutter',
            'date': '2025-02-22',
            'author': 'Diaby Nabintou',
            'excerpt': 'Tutoriel pratique : architecture légère, widgets et persistance locale pour une app ToDo.',
            'content': '<p>Ce tutoriel guide pas à pas la création d\'une application ToDo avec <strong>Flutter</strong>. Thèmes abordés :</p>\n<ul>\n<li>Architecture recommandée (separation of concerns, provider/state management minimal)</li>\n<li>Widgets essentiels et gestion de l\'état</li>\n<li>Navigation et animations simples</li>\n<li>Stockage local : choix entre SQLite et shared_preferences</li>\n<li>Tests unitaires et de widget pour assurer la qualité</li>\n</ul>\n<p>Le code fourni est prêt à être cloné et étendu — idéal pour apprendre les bases en pratique.</p>',
            'cover': '/assets/images/article-flutter.jpg',
            'slug': 'flutter-todo-app'
        },
        {
            'id': 'optimisation-seo-essentielle',
            'title': 'Optimisation SEO essentielle pour sites personnels',
            'date': '2025-04-05',
            'author': 'Diaby Nabintou',
            'excerpt': 'Checklist SEO pour améliorer la visibilité d\'un portfolio professionnel.',
            'content': '<p>Peu importe votre technologie, certaines règles SEO restent universelles. Cet article détaille :</p>\n<ul>\n<li>L\'utilisation pertinente des balises meta (title, description) et OpenGraph</li>\n<li>Structure sémantique HTML (h1..h3, articles, sections)</li>\n<li>Performance web : images optimisées, lazy-loading, temps de réponse serveur</li>\n<li>Sitemaps, robots.txt, et bonnes pratiques pour le rendu côté serveur ou l\'hydratation</li>\n<li>Mesures et suivi : Google Search Console, Lighthouse, et métriques Core Web Vitals</li>\n</ul>\n<p>Des exemples concrets et commandes pour générer un sitemap et configurer la base d\'un déploiement optimisé SEO sont fournis.</p>',
            'cover': '/assets/images/article-seo.jpg',
            'slug': 'optimisation-seo-essentielle'
        },
        {
            'id': 'git-et-deploiement',
            'title': 'Git et déploiement continu pour petits projets',
            'date': '2025-04-20',
            'author': 'Diaby Nabintou',
            'excerpt': 'Mettre en place une CI/CD simple avec GitHub Actions et déploiement sur Vercel/Netlify.',
            'content': '<p>Ce guide montre comment automatiser les déploiements pour un petit projet front-end :</p>\n<ul>\n<li>Structure d\'un workflow GitHub Actions pour build, test et déploiement</li>\n<li>Tests rapides et stratégies pour éviter les régressions</li>\n<li>Déploiement sur Vercel / Netlify, gestion des variables d\'environnement</li>\n<li>Rollbacks et observabilité minimale (logs, status checks)</li>\n</ul>\n<p>Fournit un exemple de fichier `workflow.yml` prêt à l\'emploi et des astuces pour garder la CI légère et fiable.</p>',
            'cover': '/assets/images/article-git.jpg',
            'slug': 'git-et-deploiement'
        }
    ]

    for article in articles_data:
        Article.objects.update_or_create(
            id=article['id'],
            defaults={
                'title': article['title'],
                'date': article['date'],
                'author': article['author'],
                'excerpt': article['excerpt'],
                'content': article['content'],
                'cover': article['cover'],
                'slug': article['slug'],
            }
        )
    print(f'✓ {len(articles_data)} articles loaded')


def populate_messages():
    """Populate messages"""
    messages_data = [
        {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Salut',
            'message': 'Ceci est un test',
            'received_at': '2026-03-06T09:06:27.567Z'
        },
        {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Salut',
            'message': 'Ceci est un test',
            'received_at': '2026-03-06T09:07:00.785Z'
        },
        {
            'name': 'Diaby Bintou',
            'email': 'bdby0706@gmail.com',
            'subject': 'message',
            'message': 'hi',
            'received_at': '2026-03-06T10:57:09.312Z'
        },
        {
            'name': 'Diaby Nabintou',
            'email': 'bdby0706@gmail.com',
            'subject': 'Demande',
            'message': 'hi Diaby',
            'received_at': '2026-03-06T11:11:14.289Z'
        }
    ]

    for msg in messages_data:
        received_at = datetime.fromisoformat(msg['received_at'].replace('Z', '+00:00'))
        Message.objects.get_or_create(
            name=msg['name'],
            email=msg['email'],
            subject=msg['subject'],
            message=msg['message'],
            received_at=received_at,
        )
    print(f'✓ {len(messages_data)} messages loaded')


def populate_statistics():
    """Populate statistics"""
    stats = Statistics.get_instance()
    stats.years_experience = 20
    stats.happy_clients = 400
    stats.projects_done = 7853
    stats.downloads = 2569
    stats.save()
    print('✓ Statistics loaded')


def populate_education():
    """Populate education"""
    education_data = [
        {
            'school': 'Institut Ivoirien de Technologie',
            'title': 'Licence 3 Informatique (Génie Logiciel)',
            'description': 'Formation en génie logiciel avec projets en développement web et mobile.',
            'time': 'En cours',
            'order': 0
        },
        {
            'school': 'Collège Notre Dame',
            'title': 'Baccalauréat série D',
            'description': '',
            'time': 'Diplômée en 2023',
            'order': 1
        }
    ]

    for edu in education_data:
        Education.objects.update_or_create(
            school=edu['school'],
            defaults={
                'title': edu['title'],
                'description': edu['description'],
                'time': edu['time'],
                'order': edu['order'],
            }
        )
    print(f'✓ {len(education_data)} education entries loaded')


def populate_experience():
    """Populate experience"""
    experience_data = [
        {
            'title': 'Projets universitaires — Développement web et mobile',
            'description': 'Réalisations de projets en Django (backend), Flutter (mobile) et interfaces avec Figma.',
            'time': '2022 - Présent',
            'order': 0
        },
        {
            'title': 'Stages et travaux dirigés',
            'description': 'Participation à des projets académiques centrés sur la création d\'applications et l\'UI/UX.',
            'time': '—',
            'order': 1
        }
    ]

    for exp in experience_data:
        Experience.objects.update_or_create(
            title=exp['title'],
            defaults={
                'description': exp['description'],
                'time': exp['time'],
                'order': exp['order'],
            }
        )
    print(f'✓ {len(experience_data)} experience entries loaded')


def populate_skills():
    """Populate skills"""
    skills_data = [
        {'name': 'Python / Django', 'percentage': 80, 'order': 0},
        {'name': 'Flutter / Dart', 'percentage': 75, 'order': 1},
        {'name': 'HTML / CSS', 'percentage': 90, 'order': 2},
        {'name': 'Figma / Photoshop', 'percentage': 70, 'order': 3},
    ]

    for skill in skills_data:
        Skill.objects.update_or_create(
            name=skill['name'],
            defaults={
                'percentage': skill['percentage'],
                'order': skill['order'],
            }
        )
    print(f'✓ {len(skills_data)} skills loaded')


if __name__ == '__main__':
    print('\n' + '='*50)
    print('Populating Database')
    print('='*50 + '\n')

    try:
        populate_articles()
        populate_messages()
        populate_statistics()
        populate_education()
        populate_experience()
        populate_skills()

        print('\n' + '='*50)
        print('✅ Database populated successfully!')
        print('='*50 + '\n')
    except Exception as e:
        print(f'\n❌ Error: {e}\n')
        sys.exit(1)

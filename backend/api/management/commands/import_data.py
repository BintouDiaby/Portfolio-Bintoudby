import json
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Article, Message, Statistics, Education, Experience, Skill


class Command(BaseCommand):
    help = 'Import data from a JSON export file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='Input JSON file path'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before importing'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        clear_data = options.get('clear', False)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'❌ File not found: {file_path}')
            )
            return
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR(f'❌ Invalid JSON format')
            )
            return

        # Clear existing data if requested
        if clear_data:
            self.stdout.write('🗑️  Clearing existing data...')
            Article.objects.all().delete()
            Message.objects.all().delete()
            Education.objects.all().delete()
            Experience.objects.all().delete()
            Skill.objects.all().delete()

        # Import articles
        if 'articles' in data:
            self._import_articles(data['articles'])

        # Import messages
        if 'messages' in data:
            self._import_messages(data['messages'])

        # Import statistics
        if 'statistics' in data:
            self._import_statistics(data['statistics'])

        # Import education
        if 'education' in data:
            self._import_education(data['education'])

        # Import experience
        if 'experience' in data:
            self._import_experience(data['experience'])

        # Import skills
        if 'skills' in data:
            self._import_skills(data['skills'])

        self.stdout.write(
            self.style.SUCCESS('\n✅ Data imported successfully!')
        )

    def _import_articles(self, articles_data):
        self.stdout.write('\n📄 Importing articles...')
        count = 0
        for article_data in articles_data:
            try:
                date = datetime.fromisoformat(article_data['date']).date()
                Article.objects.update_or_create(
                    id=article_data['id'],
                    defaults={
                        'title': article_data['title'],
                        'date': date,
                        'author': article_data['author'],
                        'excerpt': article_data['excerpt'],
                        'content': article_data['content'],
                        'cover': article_data.get('cover', ''),
                        'slug': article_data['slug'],
                    }
                )
                count += 1
                self.stdout.write(f'  ✓ {article_data["title"]}')
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'  ⚠️  Skipped: {article_data.get("title", "Unknown")} - {e}')
                )

        self.stdout.write(self.style.SUCCESS(f'  → {count} articles imported'))

    def _import_messages(self, messages_data):
        self.stdout.write('\n💬 Importing messages...')
        count = 0
        for msg_data in messages_data:
            try:
                received_at = datetime.fromisoformat(msg_data['received_at'])
                Message.objects.get_or_create(
                    name=msg_data['name'],
                    email=msg_data['email'],
                    subject=msg_data.get('subject', ''),
                    message=msg_data['message'],
                    received_at=received_at,
                )
                count += 1
                self.stdout.write(f'  ✓ Message from {msg_data["name"]}')
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'  ⚠️  Skipped message - {e}')
                )

        self.stdout.write(self.style.SUCCESS(f'  → {count} messages imported'))

    def _import_statistics(self, stats_data):
        self.stdout.write('\n📊 Importing statistics...')
        if not stats_data:
            return

        try:
            stats = Statistics.get_instance()
            data = stats_data[0]
            stats.years_experience = data.get('years_experience', 20)
            stats.happy_clients = data.get('happy_clients', 400)
            stats.projects_done = data.get('projects_done', 7853)
            stats.downloads = data.get('downloads', 2569)
            stats.save()
            self.stdout.write('  ✓ Statistics updated')
            self.stdout.write(self.style.SUCCESS(f'  → 1 statistics imported'))
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'  ⚠️  Failed to import statistics - {e}')
            )

    def _import_education(self, education_data):
        self.stdout.write('\n🎓 Importing education...')
        count = 0
        for edu_data in education_data:
            try:
                Education.objects.update_or_create(
                    id=edu_data['id'],
                    defaults={
                        'school': edu_data['school'],
                        'title': edu_data['title'],
                        'description': edu_data.get('description', ''),
                        'time': edu_data['time'],
                        'order': edu_data.get('order', 0),
                    }
                )
                count += 1
                self.stdout.write(f'  ✓ {edu_data["school"]}')
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'  ⚠️  Skipped - {e}')
                )

        self.stdout.write(self.style.SUCCESS(f'  → {count} education entries imported'))

    def _import_experience(self, experience_data):
        self.stdout.write('\n💼 Importing experience...')
        count = 0
        for exp_data in experience_data:
            try:
                Experience.objects.update_or_create(
                    id=exp_data['id'],
                    defaults={
                        'title': exp_data['title'],
                        'description': exp_data['description'],
                        'time': exp_data['time'],
                        'order': exp_data.get('order', 0),
                    }
                )
                count += 1
                self.stdout.write(f'  ✓ {exp_data["title"]}')
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'  ⚠️  Skipped - {e}')
                )

        self.stdout.write(self.style.SUCCESS(f'  → {count} experience entries imported'))

    def _import_skills(self, skills_data):
        self.stdout.write('\n🎯 Importing skills...')
        count = 0
        for skill_data in skills_data:
            try:
                Skill.objects.update_or_create(
                    id=skill_data['id'],
                    defaults={
                        'name': skill_data['name'],
                        'percentage': skill_data['percentage'],
                        'order': skill_data.get('order', 0),
                    }
                )
                count += 1
                self.stdout.write(f'  ✓ {skill_data["name"]}')
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'  ⚠️  Skipped - {e}')
                )

        self.stdout.write(self.style.SUCCESS(f'  → {count} skills imported'))

import json
from django.core.management.base import BaseCommand
from api.models import Article, Message, Statistics, Education, Experience, Skill


class Command(BaseCommand):
    help = 'Export all database data to a JSON file for backup and populate purposes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='data_export.json',
            help='Output file path (default: data_export.json)'
        )

    def handle(self, *args, **options):
        output_file = options['output']

        # Collect all data
        data = {
            'articles': self._export_articles(),
            'messages': self._export_messages(),
            'statistics': self._export_statistics(),
            'education': self._export_education(),
            'experience': self._export_experience(),
            'skills': self._export_skills(),
        }

        # Write to file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            self.stdout.write(
                self.style.SUCCESS(f'✅ Data exported successfully to: {output_file}')
            )
            self.stdout.write(f'\n📊 Summary:')
            self.stdout.write(f'   - Articles: {len(data["articles"])}')
            self.stdout.write(f'   - Messages: {len(data["messages"])}')
            self.stdout.write(f'   - Statistics: {len(data["statistics"])}')
            self.stdout.write(f'   - Education: {len(data["education"])}')
            self.stdout.write(f'   - Experience: {len(data["experience"])}')
            self.stdout.write(f'   - Skills: {len(data["skills"])}')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error exporting data: {e}')
            )

    def _export_articles(self):
        articles = Article.objects.all()
        return [
            {
                'id': article.id,
                'title': article.title,
                'date': article.date.isoformat(),
                'author': article.author,
                'excerpt': article.excerpt,
                'content': article.content,
                'cover': article.cover,
                'slug': article.slug,
            }
            for article in articles
        ]

    def _export_messages(self):
        messages = Message.objects.all()
        return [
            {
                'id': msg.id,
                'name': msg.name,
                'email': msg.email,
                'subject': msg.subject,
                'message': msg.message,
                'received_at': msg.received_at.isoformat(),
            }
            for msg in messages
        ]

    def _export_statistics(self):
        try:
            stats = Statistics.get_instance()
            return [
                {
                    'id': stats.id,
                    'years_experience': stats.years_experience,
                    'happy_clients': stats.happy_clients,
                    'projects_done': stats.projects_done,
                    'downloads': stats.downloads,
                    'updated_at': stats.updated_at.isoformat(),
                }
            ]
        except:
            return []

    def _export_education(self):
        education = Education.objects.all()
        return [
            {
                'id': edu.id,
                'school': edu.school,
                'title': edu.title,
                'description': edu.description,
                'time': edu.time,
                'order': edu.order,
            }
            for edu in education
        ]

    def _export_experience(self):
        experiences = Experience.objects.all()
        return [
            {
                'id': exp.id,
                'title': exp.title,
                'description': exp.description,
                'time': exp.time,
                'order': exp.order,
            }
            for exp in experiences
        ]

    def _export_skills(self):
        skills = Skill.objects.all()
        return [
            {
                'id': skill.id,
                'name': skill.name,
                'percentage': skill.percentage,
                'order': skill.order,
            }
            for skill in skills
        ]

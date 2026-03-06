import json
from pathlib import Path
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Article


class Command(BaseCommand):
    help = 'Migrate articles from articles.json to database'

    def handle(self, *args, **options):
        articles_file = Path(__file__).resolve().parent.parent.parent.parent / 'articles.json'

        if not articles_file.exists():
            self.stdout.write(self.style.ERROR(f'File not found: {articles_file}'))
            return

        try:
            with open(articles_file, 'r', encoding='utf-8') as f:
                articles_data = json.load(f)

            count = 0
            for article_data in articles_data:
                # Convert date string to date object
                if isinstance(article_data['date'], str):
                    date = datetime.fromisoformat(article_data['date']).date()
                else:
                    date = article_data['date']

                article, created = Article.objects.update_or_create(
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
                action = 'Created' if created else 'Updated'
                self.stdout.write(self.style.SUCCESS(f'{action}: {article.title}'))

            self.stdout.write(
                self.style.SUCCESS(f'Successfully migrated {count} articles')
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during migration: {e}'))

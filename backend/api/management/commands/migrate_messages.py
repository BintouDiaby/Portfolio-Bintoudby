import json
from pathlib import Path
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Message


class Command(BaseCommand):
    help = 'Migrate messages from messages.json to database'

    def handle(self, *args, **options):
        messages_file = Path(__file__).resolve().parent.parent.parent.parent / 'messages.json'

        if not messages_file.exists():
            self.stdout.write(self.style.WARNING(f'File not found: {messages_file}'))
            return

        try:
            with open(messages_file, 'r', encoding='utf-8') as f:
                messages_data = json.load(f)

            count = 0
            for msg_data in messages_data:
                # Parse received_at timestamp
                if isinstance(msg_data['receivedAt'], str):
                    received_at = datetime.fromisoformat(msg_data['receivedAt'].replace('Z', '+00:00'))
                else:
                    received_at = msg_data['receivedAt']

                Message.objects.get_or_create(
                    name=msg_data['name'],
                    email=msg_data['email'],
                    subject=msg_data.get('subject', ''),
                    message=msg_data['message'],
                    received_at=received_at,
                )
                count += 1

            self.stdout.write(
                self.style.SUCCESS(f'Successfully migrated {count} messages')
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during migration: {e}'))

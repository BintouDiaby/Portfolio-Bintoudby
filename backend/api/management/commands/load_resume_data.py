from django.core.management.base import BaseCommand
from api.models import Education, Experience, Skill


class Command(BaseCommand):
    help = 'Load initial resume data (education, experience, skills)'

    def handle(self, *args, **options):
        # Clear existing data
        Education.objects.all().delete()
        Experience.objects.all().delete()
        Skill.objects.all().delete()

        # Load education data
        education_data = [
            {
                'school': 'Institut Ivoirien de Technologie',
                'title': 'Licence 3 Informatique (Génie Logiciel)',
                'time': 'En cours',
                'description': 'Formation en génie logiciel avec projets en développement web et mobile.',
                'order': 0
            },
            {
                'school': 'Collège Notre Dame',
                'title': 'Baccalauréat série D',
                'time': 'Diplômée en 2023',
                'description': '',
                'order': 1
            },
        ]

        for edu in education_data:
            Education.objects.create(**edu)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Education: {edu["school"]} — {edu["title"]}')
            )

        # Load experience data
        experience_data = [
            {
                'title': 'Projets universitaires — Développement web et mobile',
                'time': '2022 - Présent',
                'description': 'Réalisations de projets en Django (backend), Flutter (mobile) et interfaces avec Figma.',
                'order': 0
            },
            {
                'title': 'Stages et travaux dirigés',
                'time': '—',
                'description': 'Participation à des projets académiques centrés sur la création d\'applications et l\'UI/UX.',
                'order': 1
            },
        ]

        for exp in experience_data:
            Experience.objects.create(**exp)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Experience: {exp["title"]}')
            )

        # Load skills data
        skills_data = [
            {'name': 'Python / Django', 'percentage': 80, 'order': 0},
            {'name': 'Flutter / Dart', 'percentage': 75, 'order': 1},
            {'name': 'HTML / CSS', 'percentage': 90, 'order': 2},
            {'name': 'Figma / Photoshop', 'percentage': 70, 'order': 3},
        ]

        for skill in skills_data:
            Skill.objects.create(**skill)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Skill: {skill["name"]} ({skill["percentage"]}%)')
            )

        self.stdout.write(
            self.style.SUCCESS('\n✅ Resume data loaded successfully!')
        )

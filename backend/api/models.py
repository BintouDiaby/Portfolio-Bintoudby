from django.db import models


class Statistics(models.Model):
    """Global statistics for the portfolio"""
    years_experience = models.IntegerField(default=20)
    happy_clients = models.IntegerField(default=400)
    projects_done = models.IntegerField(default=7853)
    downloads = models.IntegerField(default=2569)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Statistics"

    def __str__(self):
        return "Portfolio Statistics"

    @classmethod
    def get_instance(cls):
        """Get or create the singleton Statistics instance"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-received_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class Education(models.Model):
    """Education/Formation model"""
    title = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=255, help_text="ex: 2023, En cours, 2022 - 2023")
    order = models.IntegerField(default=0, help_text="Order of display (0 = first)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.school} — {self.title}"


class Experience(models.Model):
    """Work experience/Projets model"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.CharField(max_length=255, help_text="ex: 2022 - Présent, 2023, —")
    order = models.IntegerField(default=0, help_text="Order of display (0 = first)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Skills/Compétences model"""
    name = models.CharField(max_length=255)
    percentage = models.IntegerField(
        default=50,
        help_text="Skill level from 0 to 100"
    )
    order = models.IntegerField(default=0, help_text="Order of display (0 = first)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Article(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    author = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    cover = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import Article, Message, Statistics, Education, Experience, Skill


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin interface for Article model"""
    list_display = ('title', 'slug', 'author', 'date', 'get_excerpt_preview')
    list_filter = ('date', 'author')
    search_fields = ('title', 'slug', 'author', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('id',)

    fieldsets = (
        ('Informations principales', {
            'fields': ('id', 'title', 'slug', 'author')
        }),
        ('Contenu', {
            'fields': ('excerpt', 'content'),
            'classes': ('wide',)
        }),
        ('Médias', {
            'fields': ('cover',)
        }),
        ('Date de publication', {
            'fields': ('date',)
        }),
    )

    def get_excerpt_preview(self, obj):
        """Display excerpt preview truncated to 50 chars"""
        excerpt = obj.excerpt[:50] + '...' if len(obj.excerpt) > 50 else obj.excerpt
        return excerpt
    get_excerpt_preview.short_description = 'Aperçu'

    def save_model(self, request, obj, form, change):
        """Override save to ensure slug is set"""
        if not obj.slug and obj.title:
            # Auto-generate slug from title if not provided
            obj.slug = obj.title.lower().replace(' ', '-').replace('é', 'e').replace('è', 'e')
        super().save_model(request, obj, form, change)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin interface for Education model"""
    list_display = ('school', 'title', 'time', 'order')
    list_filter = ('order',)
    search_fields = ('school', 'title', 'description')
    ordering = ('order',)

    fieldsets = (
        ('Informations', {
            'fields': ('school', 'title', 'time')
        }),
        ('Détails', {
            'fields': ('description',),
            'classes': ('wide',)
        }),
        ('Ordre d\'affichage', {
            'fields': ('order',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Admin interface for Experience model"""
    list_display = ('title', 'time', 'order')
    list_filter = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)

    fieldsets = (
        ('Informations', {
            'fields': ('title', 'time')
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('wide',)
        }),
        ('Ordre d\'affichage', {
            'fields': ('order',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin interface for Skill model"""
    list_display = ('name', 'percentage', 'order')
    list_filter = ('order',)
    search_fields = ('name',)
    ordering = ('order',)

    fieldsets = (
        ('Compétence', {
            'fields': ('name', 'percentage')
        }),
        ('Ordre d\'affichage', {
            'fields': ('order',)
        }),
    )


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    """Admin interface for Statistics model"""
    list_display = ('years_experience', 'happy_clients', 'projects_done', 'downloads', 'updated_at')
    readonly_fields = ('updated_at',)

    fieldsets = (
        ('Statistiques du portfolio', {
            'fields': ('years_experience', 'happy_clients', 'projects_done', 'downloads')
        }),
        ('Informations', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        """Only one Statistics object should exist"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of Statistics"""
        return False


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin interface for Message model"""
    list_display = ('name', 'email', 'subject', 'received_at_formatted', 'message_preview')
    list_filter = ('received_at', 'email')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('received_at', 'message_preview_full')

    fieldsets = (
        ('Expéditeur', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message_preview_full')
        }),
        ('Date de réception', {
            'fields': ('received_at',)
        }),
    )

    def has_add_permission(self, request):
        """Prevent manual creation of messages in admin"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Allow deletion of messages"""
        return True

    def received_at_formatted(self, obj):
        """Display formatted date"""
        return obj.received_at.strftime('%d/%m/%Y %H:%M')
    received_at_formatted.short_description = 'Reçu le'

    def message_preview(self, obj):
        """Display message preview truncated to 50 chars"""
        preview = obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
        return preview
    message_preview.short_description = 'Aperçu du message'

    def message_preview_full(self, obj):
        """Display full message as readonly"""
        return obj.message
    message_preview_full.short_description = 'Message complet'

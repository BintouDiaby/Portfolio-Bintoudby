#!/usr/bin/env python
"""
Script pour créer un superuser Django interactivement
Usage: python setup_admin.py
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User


def create_superuser():
    """Create a superuser interactively"""
    print("\n" + "=" * 50)
    print("Création d'un compte administrateur Django")
    print("=" * 50 + "\n")

    # Check if superuser already exists
    if User.objects.filter(username='admin').exists():
        response = input("Un utilisateur 'admin' existe déjà. Créer un autre? (y/n): ")
        if response.lower() != 'y':
            print("Annulé.")
            return

    username = input("Nom d'utilisateur [admin]: ").strip() or 'admin'
    email = input("Email: ").strip()
    password = input("Mot de passe: ").strip()
    password_confirm = input("Confirmer le mot de passe: ").strip()

    if not email or not password:
        print("❌ Email et mot de passe sont requis!")
        return

    if password != password_confirm:
        print("❌ Les mots de passe ne correspondent pas!")
        return

    if len(password) < 6:
        print("❌ Le mot de passe doit contenir au moins 6 caractères!")
        return

    try:
        if User.objects.filter(username=username).exists():
            print(f"❌ L'utilisateur '{username}' existe déjà!")
            return

        user = User.objects.create_superuser(username, email, password)
        print(f"\n✅ Superuser '{username}' créé avec succès!")
        print(f"📧 Email: {email}")
        print(f"\n🔗 Accédez à l'admin: http://localhost:3001/admin/")
        print(f"   Username: {username}")
        print(f"   Password: (le mot de passe que vous avez entré)")

    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == '__main__':
    create_superuser()

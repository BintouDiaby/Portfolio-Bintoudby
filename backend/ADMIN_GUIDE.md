# Guide d'Administration Django

## 🔐 Accès à l'interface d'admin

### URL
```
http://localhost:3001/admin/
```

### Identifiants par défaut
- **Username**: `admin`
- **Password**: `admin123`

⚠️ **Important**: Changez le mot de passe après la première connexion!

---

## 📚 Gestion des Articles

### Ajouter un article
1. Allez dans **Articles** → **Ajouter un article**
2. Remplissez les champs:
   - **Title** (Titre): Le titre de l'article
   - **Slug** (URL): Auto-généré depuis le titre (ex: `mon-article`)
   - **Author** (Auteur): Nom de l'auteur
   - **Date**: Date de publication
   - **Excerpt** (Résumé): Court résumé (50-200 caractères)
   - **Content** (Contenu): Le contenu complet en HTML
   - **Cover** (Image de couverture): URL de l'image

### Modifier un article
1. Allez dans **Articles** → Cliquez sur l'article à modifier
2. Modifiez les champs
3. Cliquez sur **Enregistrer**

### Supprimer un article
1. Cochez la case de l'article
2. Sélectionnez **Supprimer les articles sélectionnés**
3. Confirmez

### Rechercher/filtrer
- **Recherche**: Cherchez par titre, slug, auteur ou contenu
- **Filtrer par date**: Utilisez le filtre à droite
- **Filtrer par auteur**: Utilisez le filtre à droite

---

## 💬 Gestion des Messages de Contact

### Voir les messages
1. Allez dans **Messages**
2. Vous verrez la liste de tous les messages reçus

### Colonnes affichées
- **Nom**: Nom de l'expéditeur
- **Email**: Email de l'expéditeur
- **Sujet**: Sujet du message
- **Reçu le**: Date et heure de réception
- **Aperçu**: Aperçu du message

### Consulter un message complet
1. Cliquez sur un message pour le voir en détail
2. Vous verrez le message complet (non-éditable)

### Filtrer les messages
- **Par date**: Utilisez le calendrier à droite
- **Par email**: Utilisez le filtre à droite

### Supprimer les messages
1. Cochez les messages à supprimer
2. Sélectionnez **Supprimer les messages sélectionnés**
3. Confirmez

**Note**: Vous ne pouvez pas créer de messages manuellement (ils sont générés uniquement via le formulaire de contact)

---

## 🔑 Gestion des utilisateurs

Pour ajouter d'autres administrateurs:
1. Allez dans **Authentification et autorisation** → **Utilisateurs**
2. Cliquez sur **Ajouter un utilisateur**
3. Entrez le username et le mot de passe
4. Cochez **Statut de superutilisateur** pour donner l'accès complet

---

## 🔄 Synchronisation Frontend ↔ Backend

### Quand les changements sont visibles?
1. **Cache Frontend**: Valide 24h
2. **Pour mettre à jour immédiatement**:
   - Attendez le rechargement automatique
   - Ou cliquez sur "Recharger les articles" sur le frontend

### Commande pour forcer l'expiration du cache
```bash
# Via Django shell
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

---

## 📊 Statistiques

### Récupérer le nombre d'articles et messages
```bash
python manage.py shell
>>> from api.models import Article, Message
>>> Article.objects.count()  # Nombre d'articles
>>> Message.objects.count()  # Nombre de messages
```

---

## 🚀 Tips

1. **Export de données**: Utilisez le filtre et copiez-collez les données
2. **Bulk edit**: Utilisez les actions groupées pour modifier plusieurs articles
3. **Recherche avancée**: Utilisez les filtres à droite pour des recherches précises
4. **Historique**: Django enregistre automatiquement qui a modifié quoi et quand

---

## ⚠️ Sécurité

1. **Changez le mot de passe par défaut** immédiatement
2. **Ne partagez pas l'URL admin** en production
3. **Utilisez HTTPS** en production
4. **Limitez l'accès** aux administrateurs de confiance

---

## 🆘 Dépannage

**Problème**: Impossible de se connecter
- Vérifiez votre username/password
- Assurez-vous que le serveur Django fonctionne

**Problème**: Les articles ne s'affichent pas
- Vérifiez que les articles ont une date valide
- Rechargez la page frontend

**Problème**: Oublié le mot de passe admin
```bash
python manage.py changepassword admin
```

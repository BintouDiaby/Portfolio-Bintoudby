# Backend minimal pour le portfolio

Ce backend fournit un endpoint `POST /api/contact` pour recevoir les messages du formulaire de contact.

Fonctionnalités :
- Stocke les messages dans `messages.json`.
- Optionnel : envoie un email si les variables SMTP sont définies.

Variables d'environnement (optionnelles pour l'email) :
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM`, `CONTACT_RECEIVER`, `SMTP_SECURE` (`true`/`false`)

Pour installer et lancer :

```bash
cd backend
npm install
npm start
```

Le serveur écoute par défaut sur le port `3001`.

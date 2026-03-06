# Portfolio Diaby Nabintou - Full Stack

Un portfolio professionnel avec **Django Backend** et **Angular Frontend**.

## 📁 Structure du Projet

```
Portfolio-Bintoudby/
├── backend/              # Django API (Port 3001)
│   ├── api/             # App Django avec modèles & vues
│   ├── backend/         # Configuration Django
│   ├── db.sqlite3       # Base de données
│   ├── manage.py
│   ├── populate.py      # Script pour remplir la BD
│   └── requirements.txt
│
├── frontend/            # Angular Application (Port 4200)
│   ├── src/            # Code source Angular
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   └── node_modules/
│
└── README.md           # Ce fichier
```

## 🚀 Quick Start

### 1. Backend (Django)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python populate.py        # Remplir la BD avec les données
python manage.py runserver 3001
```

**Admin**: http://localhost:3001/admin/
- Username: `admin`
- Password: `admin123`

### 2. Frontend (Angular)

```bash
cd frontend
npm install
npm start
```

**URL**: http://localhost:4200/

---

## 📊 API Endpoints

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/articles` | Liste articles |
| GET | `/api/articles/:slug` | Article détail |
| POST | `/api/contact` | Formulaire contact |
| GET | `/api/statistics` | Stats (années, clients, projets, downloads) |
| GET | `/api/resume` | Expérience (éducation, skills, projets) |

---

## 🎮 Gestion du Contenu

Tout se gère via l'**Admin Django**: http://localhost:3001/admin/

- 📝 **Articles** - Blog posts
- 💬 **Messages** - Contact form submissions
- 📊 **Statistics** - Modify portfolio metrics
- 🎓 **Education** - Formations
- 💼 **Experience** - Projets & expérience
- 🎯 **Skills** - Compétences avec %

---

## 📚 Documentation

- `backend/ADMIN_GUIDE.md` - Guide complet de l'admin Django
- `backend/API_ENDPOINTS.md` - Documentation API détaillée
- `backend/README_FULL.md` - Guide complet du projet

---

## 💾 Remplir la Base de Données

```bash
cd backend
source venv/bin/activate
python populate.py
```

Cela charge:
- ✅ 5 articles de blog
- ✅ 4 messages de contact
- ✅ 2 formations
- ✅ 2 expériences
- ✅ 4 compétences
- ✅ Les statistiques du portfolio

---

## 🔑 Credentials par Défaut

**Django Admin**:
- Username: `admin`
- Password: `admin123`

⚠️ **Changez le mot de passe en production!**

```bash
cd backend
python manage.py changepassword admin
```

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 6.0.3
- **Database**: SQLite
- **API**: REST (JsonResponse)
- **Email**: SMTP (configurable)

### Frontend
- **Framework**: Angular 20+
- **Language**: TypeScript
- **State**: Angular Signals
- **Styling**: SCSS

---

## 📱 Features

✅ Blog avec articles dynamiques
✅ Pages articles détail
✅ Section expérience/CV
✅ Formulaire contact
✅ Admin interface complète
✅ Cache localStorage (24h)
✅ Responsive design
✅ CORS enabled
✅ Email support

---

## 🚀 Déploiement

### Backend
```bash
pip install gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:3001
```

### Frontend
```bash
cd frontend
npm run build
# Output: dist/
```

---

**Status**: ✅ Fully Functional
**Last Updated**: 2026-03-06

# API Endpoints Documentation

## Base URL
```
http://localhost:3001/api/
```

## Endpoints

### 1. Health Check
**GET** `/health`

Response:
```json
{
  "ok": true
}
```

---

### 2. Articles (Blog)
**GET** `/articles`

Response:
```json
[
  {
    "id": "apprendre-django-premier-projet",
    "title": "Apprendre Django : premier projet backend",
    "date": "2025-01-15",
    "author": "Diaby Nabintou",
    "excerpt": "Guide pas-à-pas pour créer une API REST robuste...",
    "content": "<p>Contenu complet en HTML...</p>",
    "cover": "/assets/images/article-django.jpg",
    "slug": "apprendre-django-premier-projet"
  }
]
```

---

### 3. Single Article
**GET** `/articles/:slug`

Example: `/articles/apprendre-django-premier-projet`

Response: (same as single item above)

---

### 4. Contact Form
**POST** `/contact`

Request Body:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Portfolio inquiry",
  "message": "I'd like to work with you..."
}
```

Response:
```json
{
  "ok": true
}
```

Status Codes:
- `200 OK` - Message sent successfully
- `400 Bad Request` - Missing required fields
- `500 Internal Server Error` - Server error

---

### 5. Portfolio Statistics
**GET** `/statistics`

Response:
```json
{
  "years_experience": 20,
  "happy_clients": 400,
  "projects_done": 7853,
  "downloads": 2569,
  "updated_at": "2026-03-06T15:02:02.237734+00:00"
}
```

**Editable via Admin**: Yes (/admin/api/statistics/)

---

### 6. Resume Data
**GET** `/resume`

Response:
```json
{
  "education": [
    {
      "id": 1,
      "school": "Institut Ivoirien de Technologie",
      "title": "Licence 3 Informatique (Génie Logiciel)",
      "description": "Formation en génie logiciel...",
      "time": "En cours"
    }
  ],
  "experience": [
    {
      "id": 1,
      "title": "Projets universitaires — Développement web et mobile",
      "description": "Réalisations de projets en Django...",
      "time": "2022 - Présent"
    }
  ],
  "skills": [
    {
      "id": 1,
      "name": "Python / Django",
      "percentage": 80
    }
  ]
}
```

**Editable via Admin**: Yes
- `/admin/api/education/`
- `/admin/api/experience/`
- `/admin/api/skill/`

---

## CORS Configuration

Allowed origins:
- `http://localhost:4200`
- `http://localhost:3000`
- `http://127.0.0.1:4200`
- `http://127.0.0.1:3000`

To add more origins, edit `backend/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
    'http://your-domain.com',
    # ... more origins
]
```

---

## Error Handling

All endpoints return errors in this format:

```json
{
  "error": "Descriptive error message"
}
```

Common HTTP Status Codes:
- `200` - Success
- `400` - Bad Request (validation error)
- `404` - Not Found
- `500` - Server Error

---

## Frontend Integration

The frontend uses the `ArticleService` in `src/app/shared/services/article.service.ts` to interact with these endpoints.

All responses are cached in localStorage for 24 hours for offline support.

---

## Admin Interface

Access the Django admin at: `http://localhost:3001/admin/`

Credentials:
- Username: `admin`
- Password: `admin123`

Manage:
- Articles
- Messages (contact form submissions)
- Statistics
- Education
- Experience
- Skills

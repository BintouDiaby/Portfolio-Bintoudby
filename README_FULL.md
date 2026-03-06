# Portfolio Diaby Nabintou - Full Stack Setup

## 🏗️ Architecture

### Frontend (Angular 20+)
- **Framework**: Angular (Standalone Components)
- **Port**: 4200
- **Language**: TypeScript
- **Features**:
  - Blog with articles loaded from backend
  - Article detail pages
  - Experience/Resume section
  - Contact form with localStorage caching
  - Responsive design

### Backend (Django)
- **Framework**: Django 6.0.3
- **Port**: 3001 (configurable)
- **Database**: SQLite
- **Features**:
  - REST API (no DRF - plain JsonResponse)
  - 6 endpoints for articles, contact, statistics, resume
  - Django Admin interface for content management
  - CORS enabled
  - Email support (SMTP configurable)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run migrations (already done)
python manage.py migrate

# Load sample data
python manage.py load_resume_data

# Create superuser (already done: admin/admin123)
# Or create a new one:
python manage.py createsuperuser

# Start development server
python manage.py runserver 3001
```

Access Django Admin: http://localhost:3001/admin/
- Username: `admin`
- Password: `admin123`

### Frontend Setup

```bash
npm install
npm start  # or ng serve
```

Access Frontend: http://localhost:4200/

---

## 📁 Project Structure

```
Portfolio-Bintoudby/
├── backend/                          # Django backend
│   ├── api/
│   │   ├── models.py                # Article, Message, Statistics, Education, Experience, Skill
│   │   ├── views.py                 # 6 API endpoints
│   │   ├── admin.py                 # Django admin configuration
│   │   ├── urls.py                  # API routes
│   │   ├── management/commands/
│   │   │   ├── migrate_articles.py
│   │   │   ├── migrate_messages.py
│   │   │   └── load_resume_data.py
│   │   └── migrations/
│   ├── backend/
│   │   ├── settings.py              # Django settings (CORS, Email, etc)
│   │   ├── urls.py                  # Main URL router
│   │   └── wsgi.py
│   ├── manage.py
│   ├── db.sqlite3                   # Database
│   ├── requirements.txt
│   ├── .env.example                 # Environment variables template
│   ├── ADMIN_GUIDE.md               # Django Admin guide
│   ├── API_ENDPOINTS.md             # API documentation
│   └── setup_admin.py               # Create admin script
│
├── src/                             # Angular frontend
│   ├── app/
│   │   ├── home/
│   │   │   ├── components/
│   │   │   │   ├── blog/            # Blog list & article detail
│   │   │   │   ├── resume/          # Experience/CV section
│   │   │   │   ├── contact/         # Contact form
│   │   │   │   └── ... (other components)
│   │   │   └── home.ts
│   │   ├── shared/
│   │   │   ├── services/
│   │   │   │   └── article.service.ts   # Backend integration
│   │   │   └── components/
│   │   ├── app.routes.ts            # Routing (includes /blog/:slug)
│   │   └── app.ts
│   ├── styles.scss
│   └── main.ts
│
└── README_FULL.md                  # This file
```

---

## 🔌 API Endpoints

### Core Endpoints

1. **Health Check**
   ```
   GET /api/health
   ```

2. **Blog Articles**
   ```
   GET /api/articles
   GET /api/articles/:slug
   ```

3. **Contact Form**
   ```
   POST /api/contact
   ```

4. **Statistics (Years, Clients, Projects, Downloads)**
   ```
   GET /api/statistics
   ```

5. **Resume (Education, Experience, Skills)**
   ```
   GET /api/resume
   ```

For detailed documentation, see `backend/API_ENDPOINTS.md`

---

## 🎮 Managing Content via Django Admin

### Admin URL
```
http://localhost:3001/admin/
```

### Available Sections

1. **Articles** - Blog posts
   - Add, edit, delete articles
   - Auto-generate slugs from titles
   - Filter by date and author

2. **Messages** - Contact form submissions
   - View all received messages
   - Filter by date and email
   - Messages are read-only (created only via form)

3. **Statistics** - Portfolio metrics
   - Years of Experience
   - Happy Clients
   - Projects Done
   - Downloads

4. **Education** - Formations
   - Add education history
   - Reorder with "order" field

5. **Experience** - Projects & work
   - Add experience entries
   - Reorder with "order" field

6. **Skills** - Competencies
   - Add skills with proficiency (0-100%)
   - Reorder with "order" field

---

## 💾 Data Caching

### Frontend (LocalStorage)
- Articles are cached for 24 hours
- Contact messages are stored locally
- Cache can be cleared in browser DevTools

### Backend (Database)
- All data persists in SQLite
- No external database required

---

## 📧 Email Configuration

To enable email sending (optional):

1. Create `.env` file in `backend/`:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
SMTP_FROM=your-email@gmail.com
CONTACT_RECEIVER=recipient@example.com
```

2. For Gmail:
   - Enable 2-factor authentication
   - Generate an App Password: https://myaccount.google.com/apppasswords
   - Use the generated password in `SMTP_PASS`

---

## 🔐 Changing Admin Password

```bash
cd backend
source venv/bin/activate
python manage.py changepassword admin
```

---

## 📱 Frontend Features

### Blog Page
- Lists all articles from backend
- Click to read full article
- Search/filter (via backend)
- Responsive grid layout

### Resume/Experience Section
- Education history
- Work experience entries
- Skills with progress bars
- All loaded dynamically from backend

### Contact Form
- Send messages to admin email
- Messages stored in database
- LocalStorage caching
- Form validation

---

## 🛠️ Development Workflow

1. **Add a new article**:
   - Go to http://localhost:3001/admin/
   - Click "Articles" → "Add Article"
   - Fill in details
   - Save
   - Frontend automatically updates (with 24h cache)

2. **Update statistics**:
   - Go to Admin → Statistics
   - Edit numbers
   - Save
   - Frontend updates on next load

3. **Add experience**:
   - Go to Admin → Education/Experience/Skills
   - Add entries
   - Save
   - Frontend updates

---

## 🐛 Debugging

### Check Backend Status
```bash
curl http://localhost:3001/api/health
# Should return: {"ok": true}
```

### Check Articles Loading
```bash
curl http://localhost:3001/api/articles | python -m json.tool
```

### View Logs
```bash
# Backend logs appear in the terminal running Django
# Frontend logs in browser DevTools (F12)
```

### Clear Cache (Frontend)
```javascript
// In browser console:
localStorage.removeItem('portfolio_articles');
localStorage.removeItem('portfolio_message_cache');
location.reload();
```

---

## 🚀 Deployment

### Backend (Django)
```bash
# Use Gunicorn in production:
pip install gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:3001

# Or use your hosting platform (Heroku, Railway, Render, etc)
```

### Frontend (Angular)
```bash
# Build for production:
npm run build
# Output in dist/ directory
```

---

## 📚 Documentation Files

- `backend/ADMIN_GUIDE.md` - Django Admin user guide
- `backend/API_ENDPOINTS.md` - Complete API documentation
- `README_FULL.md` - This file

---

## 🆘 Troubleshooting

**Problem**: Frontend shows "Loading articles..."
- **Solution**: Check backend is running on port 3001
- **Solution**: Check CORS settings in backend/settings.py

**Problem**: Admin login doesn't work
- **Solution**: Reset password: `python manage.py changepassword admin`
- **Solution**: Create new user: `python manage.py createsuperuser`

**Problem**: Images not showing
- **Solution**: Ensure image URLs are correct in Admin
- **Solution**: For local images, place them in `src/assets/images/`

**Problem**: Articles don't update
- **Solution**: Clear browser cache or restart both servers
- **Solution**: Check SQLite database is being written to

---

## 🎯 Next Steps

1. ✅ Update admin credentials
2. ✅ Add your content via Django Admin
3. ✅ Customize styling in `src/scss/`
4. ✅ Deploy frontend and backend
5. ✅ Configure domain and SSL

---

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review Django admin for data integrity
3. Check browser console for frontend errors
4. Check terminal for backend errors

---

## 📄 License

This project is part of the Diaby Nabintou portfolio.

---

**Last Updated**: 2026-03-06
**Status**: ✅ Fully Functional

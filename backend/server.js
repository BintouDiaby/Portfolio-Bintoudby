const express = require('express');
const path = require('path');
const fs = require('fs-extra');
const cors = require('cors');
const nodemailer = require('nodemailer');
let Database = null;
let db = null;
try {
  Database = require('better-sqlite3');
} catch (e) {
  console.warn('better-sqlite3 not installed or failed to load, server will fallback to JSON storage for messages/articles. To enable SQLite, install better-sqlite3 and required build tools.');
}

const app = express();
const PORT = process.env.PORT || 3001;

// En dev, autoriser toutes les origines pour éviter les problèmes de port
app.use(cors());
app.use(express.json());

const messagesFile = path.join(__dirname, 'messages.json');
const articlesFile = path.join(__dirname, 'articles.json');

// Try to initialize SQLite if available, otherwise remain using JSON files
const dbFile = path.join(__dirname, 'data.sqlite');
if (Database) {
  try {
    db = new Database(dbFile);
    // Initialize tables
    db.prepare(`CREATE TABLE IF NOT EXISTS messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      email TEXT,
      subject TEXT,
      message TEXT,
      receivedAt TEXT
    )`).run();

    db.prepare(`CREATE TABLE IF NOT EXISTS articles (
      id TEXT PRIMARY KEY,
      title TEXT,
      date TEXT,
      author TEXT,
      excerpt TEXT,
      content TEXT,
      cover TEXT,
      slug TEXT
    )`).run();

    // Migrate articles.json into sqlite if file exists
    try {
      if (fs.existsSync(articlesFile)) {
        const raw = fs.readJsonSync(articlesFile);
        const insert = db.prepare('INSERT OR REPLACE INTO articles (id,title,date,author,excerpt,content,cover,slug) VALUES (?,?,?,?,?,?,?,?)');
        const tx = db.transaction((items) => { for (const a of items) insert.run(a.id, a.title, a.date, a.author, a.excerpt, a.content, a.cover || null, a.slug); });
        tx(raw);
      }
    } catch (err) {
      console.error('Migration articles -> sqlite failed', err);
    }
  } catch (err) {
    console.warn('Failed to initialize SQLite DB, falling back to JSON storage:', err && err.message ? err.message : err);
    db = null;
  }
}

app.post('/api/contact', async (req, res) => {
  const { name, email, subject, message } = req.body || {};
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Les champs name, email et message sont requis.' });
  }
  const receivedAt = new Date().toISOString();
  const entry = { name, email, subject, message, receivedAt };
  try {
    if (db) {
      // store in sqlite messages table
      const stmt = db.prepare('INSERT INTO messages (name,email,subject,message,receivedAt) VALUES (?,?,?,?,?)');
      stmt.run(name, email, subject || null, message, receivedAt);
    } else {
      let messages = [];
      if (await fs.pathExists(messagesFile)) messages = await fs.readJson(messagesFile);
      messages.push(entry);
      await fs.writeJson(messagesFile, messages, { spaces: 2 });
    }

    // Optionnel : envoi d'email si variables SMTP fournies
    if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
      const transporter = nodemailer.createTransport({
        host: process.env.SMTP_HOST,
        port: process.env.SMTP_PORT ? Number(process.env.SMTP_PORT) : 587,
        secure: process.env.SMTP_SECURE === 'true',
        auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
      });
      const mailOptions = {
        from: process.env.SMTP_FROM || process.env.SMTP_USER,
        // Par défaut, envoyer au mail fourni (client), sinon utiliser CONTACT_RECEIVER ou 'bdby0706@gmail.com'
        to: process.env.CONTACT_RECEIVER || 'Bdby0706@gmail.com',
        subject: `Nouveau message portfolio: ${subject || 'Sans sujet'}`,
        text: `Nom: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
      };
      const info = await transporter.sendMail(mailOptions);
      console.log('Email envoyé:', info && info.response ? info.response : info);
    }

    return res.json({ ok: true });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Erreur serveur lors de la sauvegarde.' });
  }
});

app.get('/api/health', (req, res) => res.json({ ok: true }));

app.get('/api/articles', async (req, res) => {
  try {
    if (db) {
      const rows = db.prepare('SELECT id,title,date,author,excerpt,content,cover,slug FROM articles ORDER BY date DESC').all();
      return res.json(rows);
    }
    if (!(await fs.pathExists(articlesFile))) return res.json([]);
    const articles = await fs.readJson(articlesFile);
    return res.json(articles);
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Impossible de lire les articles.' });
  }
});

app.get('/api/articles/:slug', async (req, res) => {
  try {
    const slug = req.params.slug;
    if (db) {
      const row = db.prepare('SELECT id,title,date,author,excerpt,content,cover,slug FROM articles WHERE slug = ? OR id = ? LIMIT 1').get(slug, slug);
      if (!row) return res.status(404).json({ error: 'Article introuvable' });
      return res.json(row);
    }
    if (!(await fs.pathExists(articlesFile))) return res.status(404).json({ error: 'Article introuvable' });
    const articles = await fs.readJson(articlesFile);
    const article = (articles || []).find(a => a.slug === slug || a.id === slug);
    if (!article) return res.status(404).json({ error: 'Article introuvable' });
    return res.json(article);
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Erreur serveur lors de la lecture de l\'article.' });
  }
});

app.listen(PORT, () => console.log(`Portfolio backend démarré sur :${PORT}`));

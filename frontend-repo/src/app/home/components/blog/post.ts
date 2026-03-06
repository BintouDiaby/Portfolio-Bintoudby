import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-blog-post',
  imports: [],
  templateUrl: './post.html',
  styleUrl: './post.scss',
})
export class BlogPost implements OnInit {
  article: any = null;

  ngOnInit(): void {
    const path = window.location.pathname || '';
    const parts = path.split('/').filter(Boolean);
    const slug = parts.length ? parts[parts.length - 1] : '';
    if (!slug) return this.renderNotFound();

    fetch(`http://localhost:3001/api/articles/${slug}`)
      .then(r => {
        if (!r.ok) throw new Error('not found');
        return r.json();
      })
      .then(a => { this.article = a; this.renderArticle(); })
      .catch(() => {
        // as fallback, try fetching all and find by slug
        fetch('http://localhost:3001/api/articles')
          .then(r => r.json())
          .then((list: any[]) => {
            const found = (list || []).find(x => x.slug === slug || x.id === slug);
            if (!found) return this.renderNotFound();
            this.article = found; this.renderArticle();
          })
          .catch(() => this.renderNotFound());
      });
  }

  renderArticle() {
    const container = document.querySelector('.post-container');
    if (!container || !this.article) return;
    const cover = (this.article as any).cover || '/assets/images/image.png';
    container.innerHTML = `
      <article class="mb-5">
        <h1>${this.article.title}</h1>
        <div class="meta mb-3">${this.article.date} — par ${this.article.author}</div>
        <div class="cover mb-4"><img src="${cover}" alt="${this.article.title}" class="img-fluid"></div>
        <div class="content">${this.article.content || this.article.excerpt || ''}</div>
        <div class="mt-4"><a href="/blog" class="btn btn-outline-primary">← Retour aux articles</a></div>
      </article>
    `;
  }

  renderNotFound() {
    const container = document.querySelector('.post-container');
    if (!container) return;
    container.innerHTML = `<div class="alert alert-warning">Article introuvable.</div>`;
  }
}

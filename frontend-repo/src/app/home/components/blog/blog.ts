import { Component, OnInit } from '@angular/core';

interface Article { id:string; title:string; date:string; author:string; excerpt:string; slug:string; cover?: string }

@Component({
  selector: 'app-blog',
  imports: [],
  templateUrl: './blog.html',
  styleUrl: './blog.scss',
})
export class Blog implements OnInit {
  articles: Article[] = [];

  ngOnInit(): void {
    fetch('http://localhost:3001/api/articles')
      .then(r => r.json())
      .then((data: Article[]) => { this.articles = data || []; this.renderArticles(); })
      .catch(() => { this.articles = []; this.renderArticles(); });
  }

  renderArticles() {
    const container = document.querySelector('.blog-list');
    if (!container) return;
    container.innerHTML = '';
    if (!this.articles || this.articles.length === 0) {
      container.innerHTML = `
        <div class="col-12 text-center py-5">
          <p class="lead">Aucun article pour le moment.</p>
          <button class="btn btn-outline-primary reload-articles">Recharger</button>
        </div>
      `;
      const btn = container.querySelector('.reload-articles');
      if (btn) btn.addEventListener('click', () => { this.ngOnInit(); });
      return;
    }
    this.articles.forEach(a => {
      const col = document.createElement('div');
      col.className = 'col-lg-4 col-md-12 mb-4';
      const cover = a['cover'] || '/assets/images/image.png';
      col.innerHTML = `
        <div class="news-item">
          <div class="news-cover">
            <img src="${cover}" width="800" height="530" alt="${a.title}" class="img-fluid">
          </div>
          <div class="news-content p-4">
            <div class="news-title mb-3"><a href="/blog/${a.slug}" class="blog-permalink"><h3>${a.title}</h3></a></div>
            <div class="news-meta d-flex flex-row mb-4">
              <div class="news-meta-single mr-3"><span class="mbri-calendar"></span><span class="meta-value">${a.date}</span></div>
              <div class="news-meta-single"><span class="mbri-user"></span><span class="meta-value">par <a href="#">${a.author}</a></span></div>
            </div>
            <p>${a.excerpt}</p>
            <div class="readMore"><a href="/blog/${a.slug}" class="btn btn-outline-primary">Lire la suite</a></div>
          </div>
        </div>
      `;
      container.appendChild(col);
    });
  }
  

}

import { Component, OnInit, effect } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleService, Article } from '../../../shared/services/article.service';
import { ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-blog',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './blog.html',
  styleUrl: './blog.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Blog implements OnInit {
  constructor(private articleService: ArticleService) {
    // React to articles signal changes
    effect(() => {
      const articles = this.articleService.articles();
      if (articles.length > 0) {
        this.renderArticles(articles);
      }
    });
  }

  ngOnInit(): void {
    this.loadArticles();
  }

  async loadArticles(): Promise<void> {
    const articles = await this.articleService.loadArticles();
    if (articles.length === 0) {
      this.renderEmpty();
    }
  }

  async refreshArticles(): Promise<void> {
    const articles = await this.articleService.refreshArticles();
    if (articles.length === 0) {
      this.renderEmpty();
    }
  }

  private renderArticles(articles: Article[]): void {
    const container = document.querySelector('.blog-list');
    if (!container) return;

    container.innerHTML = '';
    articles.forEach((article) => {
      const col = document.createElement('div');
      col.className = 'col-lg-4 col-md-12 mb-4';
      const cover = article.cover || '/assets/images/image.png';

      col.innerHTML = `
        <div class="news-item">
          <div class="news-cover">
            <img
              src="${this.escapeHtml(cover)}"
              width="800"
              height="530"
              alt="${this.escapeHtml(article.title)}"
              class="img-fluid"
              loading="lazy"
            >
          </div>
          <div class="news-content p-4">
            <div class="news-title mb-3">
              <a href="/blog/${this.escapeHtml(article.slug)}" class="blog-permalink">
                <h3>${this.escapeHtml(article.title)}</h3>
              </a>
            </div>
            <div class="news-meta d-flex flex-row mb-4">
              <div class="news-meta-single mr-3">
                <span class="mbri-calendar"></span>
                <span class="meta-value">${this.escapeHtml(article.date)}</span>
              </div>
              <div class="news-meta-single">
                <span class="mbri-user"></span>
                <span class="meta-value">par <a href="#">${this.escapeHtml(article.author)}</a></span>
              </div>
            </div>
            <p>${this.escapeHtml(article.excerpt)}</p>
            <div class="readMore">
              <a href="/blog/${this.escapeHtml(article.slug)}" class="btn btn-outline-primary">
                Lire la suite
              </a>
            </div>
          </div>
        </div>
      `;
      container.appendChild(col);
    });
  }

  private renderEmpty(): void {
    const container = document.querySelector('.blog-list');
    if (!container) return;

    container.innerHTML = `
      <div class="col-12 text-center py-5">
        <p class="lead">Aucun article pour le moment.</p>
        <button class="btn btn-outline-primary reload-articles">Recharger</button>
      </div>
    `;

    const btn = container.querySelector('.reload-articles');
    if (btn) {
      btn.addEventListener('click', () => this.refreshArticles());
    }
  }

  private escapeHtml(text: string): string {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

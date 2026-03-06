import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { ArticleService, Article } from '../../../shared/services/article.service';
import { ChangeDetectionStrategy, signal } from '@angular/core';

@Component({
  selector: 'app-article',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './article.html',
  styleUrl: './blog.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ArticleComponent implements OnInit {
  article = signal<Article | null>(null);
  loading = signal(true);
  error = signal<string | null>(null);

  constructor(
    private route: ActivatedRoute,
    private articleService: ArticleService
  ) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(async (params) => {
      const slug = params.get('slug');
      if (slug) {
        await this.loadArticle(slug);
      }
    });
  }

  private async loadArticle(slug: string): Promise<void> {
    this.loading.set(true);
    this.error.set(null);

    try {
      const article = await this.articleService.getArticle(slug);
      if (article) {
        this.article.set(article);
        // Update page title
        document.title = `${article.title} - Portfolio`;
      } else {
        this.error.set('Article non trouvé');
      }
    } catch (err) {
      this.error.set('Erreur lors du chargement de l\'article');
      console.error(err);
    } finally {
      this.loading.set(false);
    }
  }
}

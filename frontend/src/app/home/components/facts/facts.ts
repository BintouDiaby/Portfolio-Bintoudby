import { Component, OnInit, signal } from '@angular/core';
import { ArticleService, Statistics } from '../../../shared/services/article.service';
import { ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-facts',
  imports: [],
  templateUrl: './facts.html',
  styleUrl: './facts.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Facts implements OnInit {
  stats = signal<Statistics | null>(null);
  isLoading = signal(true);

  constructor(private articleService: ArticleService) {}

  ngOnInit(): void {
    this.loadStatistics();
  }

  private async loadStatistics(): Promise<void> {
    try {
      const data = await this.articleService.getStatistics();
      this.stats.set(data);
    } catch (error) {
      console.error('Error loading statistics:', error);
    } finally {
      this.isLoading.set(false);
    }
  }
}

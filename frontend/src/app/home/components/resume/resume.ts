import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleService, Resume as ResumeData, Education, ExperienceItem, Skill } from '../../../shared/services/article.service';
import { ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './resume.html',
  styleUrl: './resume.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Resume implements OnInit {
  resumeData = signal<ResumeData | null>(null);
  isLoading = signal(true);

  constructor(private articleService: ArticleService) {}

  ngOnInit(): void {
    this.loadResume();
  }

  private async loadResume(): Promise<void> {
    try {
      const data = await this.articleService.getResume();
      this.resumeData.set(data);
    } catch (error) {
      console.error('Error loading resume:', error);
    } finally {
      this.isLoading.set(false);
    }
  }
}

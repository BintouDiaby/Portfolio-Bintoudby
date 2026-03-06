import { Injectable } from '@angular/core';
import { signal } from '@angular/core';

export interface Article {
  id: string;
  title: string;
  date: string;
  author: string;
  excerpt: string;
  content: string;
  slug: string;
  cover?: string;
}

export interface Statistics {
  years_experience: number;
  happy_clients: number;
  projects_done: number;
  downloads: number;
  updated_at: string;
}

export interface Education {
  id: number;
  school: string;
  title: string;
  description?: string;
  time: string;
}

export interface ExperienceItem {
  id: number;
  title: string;
  description: string;
  time: string;
}

export interface Skill {
  id: number;
  name: string;
  percentage: number;
}

export interface Resume {
  education: Education[];
  experience: ExperienceItem[];
  skills: Skill[];
}

@Injectable({
  providedIn: 'root'
})
export class ArticleService {
  private apiUrl = 'http://localhost:3001/api';
  private storageKey = 'portfolio_articles';
  private messageCacheKey = 'portfolio_message_cache';

  articles = signal<Article[]>([]);
  isLoading = signal(false);

  constructor() {}

  /**
   * Fetch all articles from backend with localStorage caching
   */
  async loadArticles(): Promise<Article[]> {
    // Check localStorage first
    const cached = this.getFromCache(this.storageKey);
    if (cached) {
      this.articles.set(cached);
      return cached;
    }

    // Fetch from backend
    this.isLoading.set(true);
    try {
      const response = await fetch(`${this.apiUrl}/articles`);
      const data = await response.json();

      if (Array.isArray(data)) {
        this.articles.set(data);
        this.saveToCache(this.storageKey, data);
        return data;
      }
      return [];
    } catch (error) {
      console.error('Error loading articles:', error);
      return [];
    } finally {
      this.isLoading.set(false);
    }
  }

  /**
   * Get a single article by slug or id
   */
  async getArticle(slugOrId: string): Promise<Article | null> {
    try {
      const response = await fetch(`${this.apiUrl}/articles/${slugOrId}`);
      if (!response.ok) return null;
      return await response.json();
    } catch (error) {
      console.error('Error loading article:', error);
      return null;
    }
  }

  /**
   * Submit a contact message
   */
  async submitMessage(
    name: string,
    email: string,
    subject: string,
    message: string
  ): Promise<boolean> {
    try {
      const response = await fetch(`${this.apiUrl}/contact`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, subject, message })
      });

      if (response.ok) {
        // Cache the message in localStorage
        const cached = this.getFromCache(this.messageCacheKey) || [];
        cached.push({
          name,
          email,
          subject,
          message,
          timestamp: new Date().toISOString()
        });
        this.saveToCache(this.messageCacheKey, cached);
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error submitting message:', error);
      return false;
    }
  }

  /**
   * Get health status from backend
   */
  async checkHealth(): Promise<boolean> {
    try {
      const response = await fetch(`${this.apiUrl}/health`);
      const data = await response.json();
      return data.ok === true;
    } catch {
      return false;
    }
  }

  /**
   * Save data to localStorage
   */
  private saveToCache(key: string, data: any): void {
    try {
      const expiry = new Date().getTime() + 24 * 60 * 60 * 1000; // 24 hours
      localStorage.setItem(key, JSON.stringify({ data, expiry }));
    } catch (error) {
      console.warn('Failed to save to cache:', error);
    }
  }

  /**
   * Get data from localStorage with expiry check
   */
  private getFromCache(key: string): any | null {
    try {
      const item = localStorage.getItem(key);
      if (!item) return null;

      const { data, expiry } = JSON.parse(item);
      if (expiry && new Date().getTime() > expiry) {
        localStorage.removeItem(key);
        return null;
      }

      return data;
    } catch (error) {
      console.warn('Failed to read from cache:', error);
      return null;
    }
  }

  /**
   * Clear all cached data
   */
  clearCache(): void {
    localStorage.removeItem(this.storageKey);
    localStorage.removeItem(this.messageCacheKey);
  }

  /**
   * Force refresh articles from backend (bypass cache)
   */
  async refreshArticles(): Promise<Article[]> {
    this.clearCache();
    return this.loadArticles();
  }

  /**
   * Get portfolio statistics
   */
  async getStatistics(): Promise<Statistics | null> {
    try {
      const response = await fetch(`${this.apiUrl}/statistics`);
      if (!response.ok) return null;
      return await response.json();
    } catch (error) {
      console.error('Error loading statistics:', error);
      return null;
    }
  }

  /**
   * Get resume data (education, experience, skills)
   */
  async getResume(): Promise<Resume | null> {
    try {
      const response = await fetch(`${this.apiUrl}/resume`);
      if (!response.ok) return null;
      return await response.json();
    } catch (error) {
      console.error('Error loading resume:', error);
      return null;
    }
  }
}

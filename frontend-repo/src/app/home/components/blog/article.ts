import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-article',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './article.html',
  styleUrl: './blog.scss',
})
export class Article {
  id: string | null = null;
  article: any = null;

  articles = [
    {
      id: '1',
      title: 'Créer un site web efficace : bonnes pratiques',
      date: '10 janvier, 2025',
      author: 'M. Kouadio',
      image: '/assets/images/blog/blog1.jpg',
      content: `<p>Ce guide présente des étapes concrètes pour construire un site web professionnel : choix des couleurs, hiérarchie du contenu, optimisation mobile, et tests utilisateurs.</p>`
    },
    {
      id: '2',
      title: '9 conseils simples pour les designers',
      date: '22 mars, 2024',
      author: 'A. Traoré',
      image: '/assets/images/blog/blog2.jpg',
      content: `<p>Conseils pratiques : grilles, typographie, contraste et prototypage rapide avec Figma.</p>`
    },
    {
      id: '3',
      title: 'Comment la technologie transforme les vies',
      date: '5 avril, 2024',
      author: "S. N'Dri",
      image: '/assets/images/blog/blog3.jpg',
      content: `<p>La technologie facilite l'accès à l'éducation, à la santé et crée de nouvelles opportunités d'emploi. Exemples locaux et projets inspirants.</p>`
    }
  ];

  constructor(private route: ActivatedRoute){
    this.id = this.route.snapshot.paramMap.get('id');
    this.article = this.articles.find(a => a.id === this.id) || this.articles[0];
  }
}

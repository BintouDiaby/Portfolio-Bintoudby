import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../../../shared/services/article.service';

@Component({
  selector: 'app-contact',
  imports: [],
  templateUrl: './contact.html',
  styleUrl: './contact.scss',
})
export class Contact implements OnInit {
  constructor(private articleService: ArticleService) {}

  ngOnInit(): void {
    const form = document.getElementById('contact-form') as HTMLFormElement | null;
    const status = document.getElementById('contact-status');

    form?.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form as HTMLFormElement);

      const name = (formData.get('name') || '').toString();
      const email = (formData.get('email') || '').toString();
      const subject = (formData.get('subject') || '').toString();
      const message = (formData.get('text') || '').toString();

      if (!name || !email || !message) {
        if (status) status.textContent = 'Veuillez remplir les champs obligatoires';
        return;
      }

      if (status) status.textContent = 'Envoi en cours...';

      try {
        const success = await this.articleService.submitMessage(
          name,
          email,
          subject,
          message
        );

        if (success) {
          if (status) status.textContent = 'Message envoyé — merci !';
          (form as HTMLFormElement).reset();
        } else {
          if (status) status.textContent = 'Erreur lors de l\'envoi du message';
        }
      } catch (err) {
        if (status) status.textContent = 'Impossible de joindre le serveur';
        console.error(err);
      }
    });
  }
}

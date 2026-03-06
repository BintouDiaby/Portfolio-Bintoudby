import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-contact',
  imports: [],
  templateUrl: './contact.html',
  styleUrl: './contact.scss',
})
export class Contact implements OnInit {
  ngOnInit(): void {
    const form = document.getElementById('contact-form') as HTMLFormElement | null;
    const status = document.getElementById('contact-status');
    form?.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form as HTMLFormElement);
      const payload = {
        name: (formData.get('name') || '').toString(),
        email: (formData.get('email') || '').toString(),
        subject: (formData.get('subject') || '').toString(),
        message: (formData.get('text') || '').toString(),
      };
      if (status) status.textContent = 'Envoi en cours...';
      try {
        const res = await fetch('http://localhost:3001/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        const json = await res.json().catch(() => ({}));
        if (res.ok) {
          if (status) status.textContent = 'Message envoyé — merci !';
          (form as HTMLFormElement).reset();
        } else {
          if (status) status.textContent = json?.error || 'Erreur lors de l envoi';
        }
      } catch (err) {
        if (status) status.textContent = 'Impossible de joindre le serveur';
      }
    });
  }

}

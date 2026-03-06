
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-introduction',
  imports: [],
  templateUrl: './introduction.html',
  styleUrl: './introduction.scss',
})
export class Introduction implements OnInit {
  ngOnInit(): void {
    // attach modal handlers for CV preview
    setTimeout(() => {
      const open = document.getElementById('open-cv-preview');
      const modal = document.getElementById('cv-modal');
      const close = document.getElementById('cv-close');
      const iframe = document.getElementById('cv-iframe') as HTMLIFrameElement | null;
      if (!open || !modal) return;
      open.addEventListener('click', (e) => {
        e.preventDefault();
        modal.style.display = 'flex';
        if (iframe) iframe.src = '/assets/cv/CV-DIABY-NABINTOU.pdf';
      });
      if (close) close.addEventListener('click', () => { modal.style.display = 'none'; if (iframe) iframe.src = ''; });
      // close on backdrop click
      modal.addEventListener('click', (ev) => { if (ev.target === modal) { modal.style.display = 'none'; if (iframe) iframe.src = ''; } });
    }, 50);
  }

}

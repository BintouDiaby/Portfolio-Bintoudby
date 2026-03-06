import {Routes} from '@angular/router';
import {Home} from './home/home';
import {Notfound} from './notfound/notfound';
import { Cv } from './cv/cv';
import { Blog } from './home/components/blog/blog';
import { ArticleComponent } from './home/components/blog/article';

export const routes: Routes = [
  {
    path: '',
    component: Home
  },
  {
    path: 'blog',
    component: Blog
  },
  {
    path: 'blog/:slug',
    component: ArticleComponent
  },
  {
    path: 'not-found',
    component: Notfound
  },
  {
    path: 'cv',
    component: Cv
  },
  {
    path: '**',
    redirectTo: '/not-found'
  }
];

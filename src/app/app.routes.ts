import {Routes} from '@angular/router';
import {Home} from './home/home';
import {Notfound} from './notfound/notfound';
import { Cv } from './cv/cv';

export const routes: Routes = [
  {
    path: '',
    component: Home
  },
  {
    path: 'not-found',
    component: Notfound
  },
  // Blog routes removed
  {
    path: 'cv',
    component: Cv
  },
  {
    path: '**',
    redirectTo: '/not-found'
  }
];

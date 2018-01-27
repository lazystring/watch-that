import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CreateComponent } from './create/create.component';
import { GroupComponent } from './group/group.component';


const routes: Routes = [
  { path: '', redirectTo: '/create', pathMatch: 'full' },
  { path: 'group/:group_id', component: GroupComponent },
  { path: 'create', component: CreateComponent },
]

@NgModule({
  exports: [
    RouterModule
  ],
  imports: [
    RouterModule.forRoot(routes)
  ],
  declarations: []
})
export class AppRoutingModule {}

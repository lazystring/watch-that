import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
  group_name: string;

  constructor(private router: Router) { }

  ngOnInit() {

  }

  createGroup() {
    this.router.navigate(['/group', this.group_name]);
  }

}

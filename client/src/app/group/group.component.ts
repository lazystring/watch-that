import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {
  group_id: string;

  constructor(
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.group_id = this.route.snapshot.paramMap.get('group_id')
  }

}

import { Component, OnInit } from '@angular/core';
import {User} from '../user';
import { UsersService } from '../users.service';


@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {

  
  newName: string = "";
  users : User[] = [];
  loaded: boolean = false;
  constructor(private usersService: UsersService) { }

  ngOnInit(): void {
    return this.getUsers();
  }

  

  getUsers(): void{
    this.usersService.getUsers().subscribe(users =>{
      console.log(users);
      this.users = users;
    })
  }

}

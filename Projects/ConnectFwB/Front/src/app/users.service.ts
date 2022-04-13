import { Injectable } from '@angular/core';
import { User } from './user';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  ROOT_URL = 'http://127.0.0.1:8000/api';
  constructor(private client: HttpClient) { }

  getUsers(): Observable<User[]> {
    return this.client.get<User[]>(`${this.ROOT_URL}/users/`);
  }

  getUser(id : any) : Observable<User> {
    return this.client.get<User>(`${this.ROOT_URL}/users/${id}`);
  }

}

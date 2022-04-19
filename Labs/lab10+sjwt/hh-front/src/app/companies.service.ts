import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Token, Company, Vacancy} from './models';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  ROOT_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }

  login(username: string, password: string) : Observable<Token>{
    return this.client.post<Token>(`${this.ROOT_URL}/login/`, {
      username,
      password
    });
  }

  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]>(`${this.ROOT_URL}/companies/`);
  }

  addCompany(company: Company): Observable<Company>{
    return this.client.post<Company>(`${this.ROOT_URL}/companies/`, company);
  }

  getCompany(id: number): Observable<Company>{
    return this.client.get<Company>(`${this.ROOT_URL}/companies/${id}/`);
  }

  getVacancies(id: number): Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`${this.ROOT_URL}/companies/${id}/vacancies/`);
  }
}

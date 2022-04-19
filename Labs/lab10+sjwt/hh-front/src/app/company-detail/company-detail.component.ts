import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CompaniesService } from '../companies.service';
import { Company, Vacancy } from '../models';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.scss']
})
export class CompanyDetailComponent implements OnInit {

  loaded!: boolean 
  company!: Company;
  vacancies: Vacancy[] = [];

  constructor(private service: CompaniesService,
    private route: ActivatedRoute,
    private location: Location) { }

  ngOnInit() {
    this.getCompany();
    this.getVacancies();
  }

  getCompany() {
    this.route.paramMap.subscribe(params => {
      const id = +(params.get('id') || '0');
      this.loaded = false;
      this.service.getCompany(id).subscribe(company => {
        this.company = company;
        this.loaded = true;
      });
    });
  }

  getVacancies(){
    this.route.paramMap.subscribe(params => {
      const id = +(params.get('id') || '0');
      this.loaded = false;
      this.service.getVacancies(id).subscribe(vacancies => {
        this.vacancies = vacancies;
        this.loaded = true;
      });
    });
  }

  back(){
    this.location.back();
  }

}

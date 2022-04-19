import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CompaniesService } from '../companies.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.scss']
})
export class CompaniesComponent implements OnInit {

  companies: Company[] = [];
  newName: string = '';
  newDesc: string = '';
  newCity: string = '';
  newAddress: string = '';

  constructor(private service: CompaniesService) { }


  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies() {
    this.service.getCompanies().subscribe(companies => {
      this.companies = companies;
    });
  }

  addCompany(){
    this.newName = this.newName.trim();
    this.newDesc = this.newDesc.trim();
    this.newCity = this.newCity.trim();
    this.newAddress = this.newAddress.trim();

    if(!this.newName || !this.newAddress || !this.newCity || !this.newDesc) return;

    const company = {
      name: this.newName,
      description: this.newDesc,
      city: this.newCity,
      address: this.newAddress,
    };

    this.newName = '';
    this.newDesc = '';
    this.newCity = '';
    this.newAddress = '';
    
    this.service.addCompany(company as Company).subscribe(company => {
      console.log(company);
      this.companies.push(company);
    })
  }

}

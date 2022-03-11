import { Component, OnInit } from '@angular/core';
import { Product, products } from '../products'

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products = products;
  constructor() {}
  
  ngOnInit(): void {
  }

  getItems(): Product[] {
    return products;
  }
}

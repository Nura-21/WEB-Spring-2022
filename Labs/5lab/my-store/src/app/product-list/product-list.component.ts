import { Component, OnInit, Input } from '@angular/core';
import { Product, products } from '../products'
import { Category, categories } from '../categories';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products = products;
  @Input() declare category: Category;
  categories: Category[];
  selectedCategory: any;

  constructor() {
    this.categories = categories;
    this.selectedCategory = categories[0];
  }
  
  ngOnInit(): void {
  }

  getItems(): Product[] {
    return this.products;
  }

  onItemRemove(product: Product): void {
    this.products = this.products.filter(x => x !== product);
  }
}

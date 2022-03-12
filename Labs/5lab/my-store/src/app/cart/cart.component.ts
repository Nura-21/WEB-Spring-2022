import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { CartService } from '../cart.service';
import {Product, products } from '../products';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  items = this.cartService.getItems();

  @Input() declare product: Product;
  @Output() remove = new EventEmitter();

  
  constructor(
    private cartService: CartService,

  ) {}


  ngOnInit(): void {
  }

  getSum(): number {
    var sum = 0;
    for(var i = 0; i < this.items.length; i++) {
      sum += this.items[i].price;
    }
    return sum;
  }

  removeItem(product: Product): void {
    this.items = this.items.filter(x => x !== product);
  }

}

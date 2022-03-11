import { Component, OnInit } from '@angular/core';
import { CartService } from '../cart.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  items = this.cartService.getItems();

  constructor(
    private cartService: CartService
  ) { }

  ngOnInit(): void {
  }

  getSum(): number {
    var sum = 0;
    for(var i = 0; i < this.items.length; i++) {
      sum += this.items[i].price;
    }
    return sum;
  }

}

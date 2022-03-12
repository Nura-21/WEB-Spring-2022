import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { Product, products } from '../products'
import { ActivatedRoute } from '@angular/router';
import { CartService } from '../cart.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  @Input() declare product: Product;
  @Input() declare catId: number;
  @Output() remove = new EventEmitter();
  constructor(
    // private route: ActivatedRoute,
    private cartService: CartService
  ) { }

  ngOnInit(): void {
  }

  getRating(): number {
    return Math.round(this.product.rate);
  }

  getShareLink(): string {
    return `https://t.me/share/url?url=${this.product.link}&text=${'Вот, что я нашел на Amazon!'}`;
  }

  addToCart(product: Product) {
    this.cartService.addToCart(product);
    // window.alert('Your product has been added to the cart!');
  }

  removeItem(product: Product): any {
    this.remove.emit(product);
  }

  addLike(): void {
    this.product.likes++;
  }

}

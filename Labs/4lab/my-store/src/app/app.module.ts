import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductItemComponent } from './product-item/product-item.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ShippingComponent } from './shipping/shipping.component';
import { CartComponent } from './cart/cart.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ProductItemComponent,
    ProductListComponent,
    ShippingComponent,
    CartComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    RouterModule.forRoot([
      {path: '', component: ProductListComponent},
      {path: 'cart', component: CartComponent },
      {path: 'shipping', component: ShippingComponent},
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarCardComponent } from '../../components/car-card/car-card.component';
import { RouterModule } from '@angular/router';
import { Vehicle, CarService } from '../../services/car.service'; //

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  standalone: true,
  imports: [CarCardComponent, CommonModule, RouterModule]
})
export class HomeComponent {
  advantages = [
    { icon: 'assets/images/icon1.png', title: 'Филиалы в трех городах', description: 'Автомобили в Алматы, Астане и Шымкенте' },
    { icon: 'assets/images/icon2.png', title: 'Приятные цены', description: 'От 15 000 ₸ в день, с разбивкой платежей для долгой аренды' },
    { icon: 'assets/images/icon3.png', title: 'Быстрое оформление', description: 'Арендуйте автомобиль всего за 10 минут' },
    { icon: 'assets/images/icon4.png', title: 'Поддержка в дороге', description: 'Мы всегда на связи, где бы вы ни оказались' }
  ];

  vehicles: Vehicle[] = []; 

  constructor(private carService: CarService) { }

  ngOnInit(): void {
    this.carService.getVehicles().subscribe(data => {
      this.vehicles = data.slice(0, 4);
    });
  }
  openWhatsApp(): void {
  const phone = '77073592980'; // без +
  const message = 'Здравствуйте! Хочу арендовать авто';
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  window.open(url, '_blank');
}


}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { StorageHelperService } from './storage-helper.service';
import { FormGroup } from '@angular/forms';

// Интерфейс для User
export interface User {
  userID: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  name: string;
  phoneNumber: string;
  address: string;
  userType: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000/api/auth/';
  private apiUrl2 = 'http://localhost:8000/api/users/users/';

  constructor(private http: HttpClient, private storageHelper: StorageHelperService) {}

  login(username: string, password: string): Observable<any> {
    return this.http.post(this.apiUrl + 'login/', { username, password }).pipe(
      tap((res: any) => {
        this.storageHelper.setItem('token', res.access); 
        this.storageHelper.setItem('user', JSON.stringify(res.user));
      })
    );
  }

  register(data: any): Observable<any> {
    return this.http.post(this.apiUrl + 'register/', data);
  }

  logout(): void {
    this.storageHelper.removeItem('token');  
  }

  isAuthenticated(): boolean {
    return !!this.storageHelper.getItem('token');  
  }

  getUserProfile(): Observable<User> {
    return this.http.get<User>(this.apiUrl2 + 'me/');
  }
  updateProfile(data: Partial<User>): Observable<User> {
    const token = this.getToken();
  
    return this.http.put<User>(this.apiUrl2 + 'me/', data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
  }
  // updateProfile(data: FormGroup): Observable<User> {
  //   const token = this.getToken();
  //   const headers = token ? { Authorization: `Bearer ${token}` } : {};
  
  //   return this.http.put<User>(this.apiUrl2 + 'me/', data.getRawValue(), { headers });
  // }

  // updateProfile(data: Partial<User>): Observable<User> {
  //   return this.http.put<User>(this.apiUrl2 + 'me/', data);
  // }

  getToken(): string | null {
    return this.storageHelper.getItem('token'); 
  }
  // private tokenKey = 'authToken';

  // getAuthToken(): string | null {
  //   return localStorage.getItem(this.tokenKey);  // Получаем токен из localStorage
  // }
}

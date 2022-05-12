from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    adress = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.FloatField(null=False)
    stock = models.IntegerField(null=False)

    def actualizar_stock(self, n):
        self.stock = self.stock + n
    
    def actualizar_precio(self, n):
        self.precio = n 
    
    def get_price(self):
        return self.price

    def __str__(self):
        return self.name

class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    date=models.DateField(auto_now_add=True)
    status_posibles = [
        ('D', 'Delivered'),
        ('P', 'Pending'),
        ('C', 'Cancel'),
    ]

    status = models.CharField(max_length=1, choices=status_posibles, default='P')

   

    def confirm_order(self):
        self.status = 'D'

    
    def cancel_order(self):
        self.status = 'C'

    def __str__(self):
        return f'{self.quantity} {self.product_id} order by: {self.client_id}'
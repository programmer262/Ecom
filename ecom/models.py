from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    Description = models.TextField(max_length=200000000000000000000)
    view = models.ImageField(null=True, blank=True)
    list1 = models.CharField(max_length=2000,null=True,blank=True)
    list2 = models.CharField(max_length=2000,null=True,blank=True)
    list3 = models.CharField(max_length=2000,null=True,blank=True)
    list4 = models.CharField(max_length=2000,null=True,blank=True)
    list5 = models.CharField(max_length=2000,null=True,blank=True)
    list6 = models.CharField(max_length=2000,null=True,blank=True)
    list7 = models.CharField(max_length=2000,null=True,blank=True)
    list8 = models.CharField(max_length=2000,null=True,blank=True)
    list9 = models.CharField(max_length=2000,null=True,blank=True)
    list10 = models.CharField(max_length=2000,null=True,blank=True)
    list11 = models.CharField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    livraison = models.CharField(max_length=50, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address


class Information(models.Model):  
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    livraison = models.CharField(max_length=50, null=True, blank=True)
    suggestion=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
        
class Contact(models.Model):  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_account = models.CharField(max_length=100)
    Message = models.TextField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name        
class Company_slider(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=100)
    description = models.TextField()
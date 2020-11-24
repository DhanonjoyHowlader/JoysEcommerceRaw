from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
        RATING_OPTIONS = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        )
        Rating = models.CharField(max_length=10, choices=RATING_OPTIONS, default='4')
        Comment = models.TextField(blank=True, null=True)

        Username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

        def __str__(self):
            return self.Username.username + " - " + self.Rating


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    STOCK = 1
    OUT = 2
    STATUS_CHOICES = [(STOCK, 'In Stock'), (OUT, 'Out of Stock')]
    status = models.IntegerField(choices=STATUS_CHOICES)

    image = models.ImageField(upload_to='products/images/', blank=True, default="products/images/default.jpg")
    file = models.FileField(upload_to='products/files/', blank=True, null=True, default='products/files/default.pdf')

    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Username.username


class Order(models.Model):

    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Payment on delivery', 'Payment on delivery')
    )
    payment_options = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Payment on delivery')
    is_paid = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=30, null =True, blank=True)

    def __str__(self):
        return self.Username.username + "-" + self.product.name + "-" + self.status


class Slider(models.Model):
    slider_1 = models.ImageField(upload_to='slider/', blank=True)
    slider_1_info = models.TextField(blank=True)
    slider_2 = models.ImageField(upload_to='slider/', blank=True)
    slider_2_info = models.TextField(blank=True)
    slider_3 = models.ImageField(upload_to='slider/', blank=True)
    slider_3_info = models.TextField(blank=True)


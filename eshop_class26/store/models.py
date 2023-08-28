from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProfileImage', default='no_profile.png')
    address  = models.CharField(max_length = 250)
    phone  = models.CharField(max_length = 15)
    
    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username



class Banner(models.Model):
    title  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='Banner')
    http_link  = models.URLField(max_length = 200)
    ordering  = models.IntegerField(default=1)
    
    
    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title


class Category(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='Category')
    main_category  = models.ForeignKey('self', on_delete=models.CASCADE ,related_name='sub_category', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name  = models.CharField(max_length = 150)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True,null=True)
    stock_quantity = models.IntegerField()
    description  = RichTextUploadingField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity  = models.IntegerField(default=1)
    

    def __str__(self):
        return self.user.username + ' / ' + self.product.name


class OrderedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ManyToManyField(CartProduct)
    ordered  = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)
    total_amount = models.CharField(max_length = 150,blank=True,null=True)
    payment_method  = models.CharField(max_length = 150,blank=True,null=True)
    orderedID  = models.CharField(max_length = 150,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    
    
    
    
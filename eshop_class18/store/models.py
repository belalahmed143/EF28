from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
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


from django.contrib import admin
from .models import *
# Register your models here.
my_model_list = [Banner,Category,Product,Contact]

admin.site.register(my_model_list)

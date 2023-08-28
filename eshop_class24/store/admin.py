from django.contrib import admin
from .models import *
# Register your models here.

all_model = [Category,Banner,Product,Profile]

admin.site.register(all_model)
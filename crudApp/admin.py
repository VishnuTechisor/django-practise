# from django.contrib import admin
# from .models import *

# # Register your models here.

# admin.site.register(userModel)

from django.contrib import admin

from .models import *

admin.site.register(userModel)
admin.site.register(blogModel)
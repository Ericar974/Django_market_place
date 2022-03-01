from attr import field
from django.contrib import admin

from .models import Test
# Register your models here.
class TestAdmin(admin.ModelAdmin):
    fields=['date','text', 'price', 'img', 'stock', 'description']

admin.site.register(Test)
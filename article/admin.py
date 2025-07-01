from django.contrib import admin
from .models import Articleitem
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display= ("title","description", "mainTF")
    

admin.site.register(Articleitem ,ArticleAdmin)
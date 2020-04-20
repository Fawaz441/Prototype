from django.contrib import admin
from .models import Offer,Post
# from django.contrib.admin.models import 

class offerAdmin(admin.ModelAdmin):
    list_display = ['client_name','service','email','created_at','number']

# admin.site.unregister(Group)
admin.site.register(Offer,offerAdmin)
admin.site.register(Post)

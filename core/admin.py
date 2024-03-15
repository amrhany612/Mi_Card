from django.contrib import admin
from .models import CustomUser,Categories,SubCategory,Brand,Branches


admin.site.register(CustomUser)
admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Branches)



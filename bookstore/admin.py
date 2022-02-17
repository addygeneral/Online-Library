from django.contrib import admin
from bookstore.models import User, Book, MakeRequest, Chat

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(MakeRequest)
admin.site.register(Chat)
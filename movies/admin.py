from django.contrib import admin

from movies.models import  Faviorites, Genre, Movies

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(Faviorites)

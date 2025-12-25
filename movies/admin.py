from django.contrib import admin

from movies.models import  Contact, Faviorites, Genre, Movies, Reviews

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(Faviorites)
admin.site.register(Contact)

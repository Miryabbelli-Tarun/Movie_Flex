
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('new-movies/',views.new_movies,name='new_movies'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('help/',views.help,name='help'),
    path('movie/<int:id>/',views.detail_view,name='detail_view'),
    path('profile/',views.profile_view,name='profile_view'),
    path('edit-profile/<int:id>',views.edit_profile,name='edit_profile'),
    path('faviorites/',views.faviorites,name='faviorites'),
    path('add-to-faviorites/<int:id>/',views.add_to_faviorites,name='add_to_faviorites'),
]

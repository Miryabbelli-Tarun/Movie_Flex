from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title=models.CharField(max_length=150)
    hero_name=models.CharField(max_length=100,default='Unknown')
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True,blank=True)
    rating=models.IntegerField()
    relese_date=models.DateField(null=True,blank=True)
    genres=models.ManyToManyField(Genre,blank=True,null=True)

    def __str__(self):
        return self.title



class Reviews(models.Model):
    movie_name=models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='movie_name')
    person_name=models.CharField(max_length=100)
    comment=models.TextField()
    comment_at=models.DateField(auto_now_add=True)

class Faviorites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='faviorites')
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='faviorite_by')

    class Meta:
        unique_together=('user','movie')

    def __str__(self):
        return f'{self.user}-{self.movie}'
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    problem=models.TextField()

    def __str__(self):
        return self.name


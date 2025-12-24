from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register_user(User):
    
    login_email=models.EmailField(max_length=100,unique=True)
    

    def __str__(self):
        return self.first_name
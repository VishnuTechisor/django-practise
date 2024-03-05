
from datetime import datetime
from django.db import models

 # Create your models here.

class userModel(models.Model):
      eid=models.CharField(max_length=50)
      name=models.CharField(max_length=50)
      email=models.CharField(max_length= 100)
      contact=models.CharField(max_length=15)
      def __str__(self) -> str:
           return self.name
      
      
      
      
class blogModel(models.Model):
      title=models.CharField(max_length=50) 
      image=models.ImageField(upload_to="images/")   
      video=models.FileField( upload_to="media/")  
      description=models.TextField()
      author=models.CharField(max_length=50)
      createdAt=models.DateTimeField(default=datetime.now)
      def __str__(self):
         return self.title
     
      
      
from django.db import models
from model_mixin.model_mixin import SimpleBaseModel
# Create your models here.

class Resturant(SimpleBaseModel): 
    name = models.CharField(max_length=250,blank=False,unique=True) 
    def __str__(self) -> str:
         return self.name
             
    class Meta:
        db_table = 'resturants'
        ordering = ['id']    
        
        
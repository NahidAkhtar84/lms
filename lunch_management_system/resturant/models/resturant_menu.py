from django.db import models
from model_mixin.model_mixin import SimpleBaseModel
from .resturant import Resturant
# Create your models here.

class ResturantMenu(SimpleBaseModel): 
    name = models.CharField(max_length=250,blank=False)
    menu_date = models.DateField(blank=False) 
    resturant = models.ForeignKey(Resturant,related_name="resturant_menus",on_delete=models.RESTRICT)
    def __str__(self) -> str:
         return self.name
             
    class Meta:
        db_table = 'resturant_menus'
        unique_together = ('menu_date','resturant')
        ordering = ['id']    
        
        
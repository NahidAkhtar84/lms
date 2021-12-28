from django.db import models
from model_mixin.model_mixin import SimpleBaseModel
from .resturant_menu import ResturantMenu
# Create your models here.

class ResturantMenuItem(models.Model): 
    name = models.CharField(max_length=250,blank=False) 
    description = models.TextField()
    resturant_menu = models.ForeignKey(ResturantMenu,related_name="resturant_menu_item",on_delete=models.RESTRICT)
    def __str__(self) -> str:
         return self.name
             
    class Meta:
        db_table = 'resturant_menu_items'
        unique_together = ("name","resturant_menu_id")
        ordering = ['id']    
        
        
from django.db import models
from model_mixin.model_mixin import SimpleBaseModel
from .resturant import Resturant
# Create your models here.

class ChampionResturant(SimpleBaseModel): 
    resturant = models.ForeignKey(Resturant,related_name="champio_resturant",on_delete=models.RESTRICT)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
         return "{}-{}".format(self.resturant, self.date)
             
    class Meta:
        db_table = 'champion_resturants'
        unique_together = ('date','resturant')
        ordering = ['id']
        
        
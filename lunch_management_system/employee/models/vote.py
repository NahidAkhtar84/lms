from django.db import models
from model_mixin.model_mixin import SimpleBaseModel
from resturant.models.resturant import Resturant
from django.contrib.auth.models import User

class Vote(SimpleBaseModel):
    employee = models.ForeignKey(User, related_name="voting_employee", on_delete=models.RESTRICT)
    resturant = models.ForeignKey(Resturant, related_name="voted_resturant",on_delete=models.RESTRICT)
    voting_date = models.DateField(auto_now_add=True)
    vote = models.BooleanField(default=False)
    def __str__(self) -> str:
         return "{}-employee_id: {}-restaurant_id: {}".format(self.voting_date, self.employee, self.resturant)
             
    class Meta:
        db_table = 'votes'
        unique_together = ('voting_date', 'employee')
        ordering = ['id']
        
        
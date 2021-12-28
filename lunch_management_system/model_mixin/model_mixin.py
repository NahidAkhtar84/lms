from django.db import models
# from employee.models.user import User
from django.contrib import admin

class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_by = models.ForeignKey("employee.User",editable=False,related_name='created_by_%(class)s_related',on_delete=models.CASCADE)
    updated_by = models.ForeignKey("employee.User",editable=False,related_name='updated_by_%(class)s_related',on_delete=models.CASCADE)
    deleted_by = models.ForeignKey("employee.User",editable=False,related_name='deleted_by_%(class)s_related',on_delete=models.CASCADE,null=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


class SimpleBaseModel(BaseModel):
    class Meta:
        abstract = True
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)          


class BaseAdminModel(admin.ModelAdmin):
    
     def save_model(self, request, obj, form, change) -> None:
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user 
        obj.updated_by = request.user   
        obj.save()
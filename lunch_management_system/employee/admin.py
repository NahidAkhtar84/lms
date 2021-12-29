from django.contrib import admin
from employee.models import vote

admin.site.register(vote.Vote)

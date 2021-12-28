from django.contrib import admin
from employee.models import user, vote


admin.site.register(user.User)
admin.site.register(vote.Vote)

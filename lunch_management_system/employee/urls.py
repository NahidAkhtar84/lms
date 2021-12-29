from django.urls import path, include
from employee import  views

app_name = "employee"

urlpatterns = [
    path('', views.EmployeeAPIView.as_view(), name="employee"),
    path('vote/', views.VoteAPIView.as_view()),
    path('<int:pk>/', views.EmployeeAPIView.as_view(), name="employee-detail")
]

from django.urls import path, include
from employee import  views

app_name = "employee"

urlpatterns = [
    path('', views.EmployeeAPIView.as_view(), name="employee"),
    path('vote/', views.VoteAPIView.as_view()),
    # path('<int:pk>/', views.ResturantDetail.as_view()),
    # path('resturant_for_vote/',views.ResturantListForVoteView.as_view())
]

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from resturant import views

app_name = "resturant"
urlpatterns = [
    path('', views.ResturantList.as_view(), name="resturant"),
    path('<int:pk>/', views.ResturantDetail.as_view()),
    path('menu/',views.ResturantMenuList.as_view()),
    path('resturant_for_vote/',views.ResturantListForVoteView.as_view()),
    path('champion_resturant/', views.ChampionResturants.as_view()),
    path('champion_resturant/find', views.FindChampionResturant.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)

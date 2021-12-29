import json
from django.utils import timezone
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.db.models import Count, Max
from employee.models.vote import Vote
from datetime import date, timedelta
from resturant.models.resturant import Resturant
from resturant.models.champion_resturant import ChampionResturant

from resturant.models import resturant,resturant_menu,resturant_menu_item
from resturant.serializers import resturant_serializers,resturant_menu_serializers,resturant_menu_item_serializers, champion_resturant_serializers


class ResturantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]    
    serializer_class = resturant_serializers.ResturantSerializer
    queryset =resturant.Resturant.objects.all()  
    def perform_update(self, serializer_class):
            print(self.request.user)
            return serializer_class.save(updated_by=self.request.user) 
             
class ResturantList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]    
    serializer_class = resturant_serializers.ResturantSerializer
    queryset =resturant.Resturant.objects.all() 
     
    def perform_create(self, serializer_class):
            return serializer_class.save(created_by=self.request.user,updated_by=self.request.user)

class ResturantMenuList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]    
    serializer_class = resturant_menu_serializers.ResturantMenuSerializer
    queryset =resturant_menu.ResturantMenu.objects.all() 
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
             serializer.save(created_by=self.request.user,updated_by=self.request.user)
             data=serializer.data
        else:
            data['error'] = serializer.errors
        return Response(data,status=status.HTTP_201_CREATED)

class ResturantListForVoteView(generics.ListAPIView):
    now = timezone.now()
    permission_classes = [IsAuthenticated]    
    serializer_class = resturant_menu_serializers.ResturantMenuVoteSerializer
    queryset =resturant_menu.ResturantMenu.objects.select_related("resturant").filter(menu_date=now).all()             

# class ResturantListForVoteView(generics.ListAPIView):
#     now = timezone.now()
#     permission_classes = [IsAuthenticated]    
#     serializer_class = resturant_serializers.ResturantListForVoteSerializer
#     #queryset =resturant.Resturant.objects.all()
#     queryset =resturant_menu.Resturant.objects.filter(resturant_menus__menu_date=now).all()  
# 

class ChampionResturants(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk=None, format=None):
        resturant_list_with_count = Vote.objects.filter(vote=True, voting_date=date.today()).\
            values("resturant").annotate(Count("vote")).order_by("-vote__count")

        whole_list = list(resturant_list_with_count)
        expected_list = []
        pass_vote = 0
        for dict in whole_list:
            if dict["vote__count"] < pass_vote:
                break
            champion_yesterday = ChampionResturant.objects.\
                filter(resturant=dict["resturant"], date=date.today()-timedelta(1)).first()
            champion_day_before_yesterday = ChampionResturant.objects.\
                filter(resturant=dict["resturant"], date=date.today()-timedelta(2)).first()

            if not champion_yesterday or not champion_day_before_yesterday:
                expected_list.append(dict)
                pass_vote=dict["vote__count"]
        try:
            prev_champ = ChampionResturant.objects.filter(date=date.today()).delete()
        except:
            pass
        try:
            _vote_count = expected_list[0]["vote__count"]
        except:
            _vote_count = 0
        
        result_list = []
        for dict in expected_list:
            resturant_object = Resturant.objects.get(id=dict["resturant"])
            result_list.append(resturant_object)
            data = {
                "resturant": resturant_object.id
            }
            
            champion_serializer = champion_resturant_serializers.ChampionSerializer(data=data)
            
            
            if champion_serializer.is_valid():
                try:
                    champion_serializer.save(created_by=request.user, updated_by=request.user)
                except:
                    return Response({"detail": "Champions saved before!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
               return Response({"detail": "Champions could not save!"}, status=status.HTTP_400_BAD_REQUEST) 
            
        serializer = resturant_serializers.ChampionResturantSerializer(result_list, many=True, context={'vote_count': _vote_count})
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

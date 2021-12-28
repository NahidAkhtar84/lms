from rest_framework import serializers
from resturant.models.resturant_menu import ResturantMenu
from resturant.models.resturant_menu_item import ResturantMenuItem
from resturant.serializers.resturant_menu_item_serializers import ResturantMenuItemSerializer
from resturant.serializers.resturant_serializers import ResturantSerializer


class ResturantMenuSerializer(serializers.ModelSerializer):
    resturant_menu_item = ResturantMenuItemSerializer(many=True)
    class Meta:
        model = ResturantMenu
        fields = ["id","resturant","name","description","status","menu_date","resturant_menu_item"]

    def create(self, validated_data):
         resturent_menu_item = validated_data.pop("resturant_menu_item")
         resturent_menu_info = super().create(validated_data)
         for menu_item in resturent_menu_item:
             ResturantMenuItem.objects.create(resturant_menu=resturent_menu_info,**menu_item)
               
         return resturent_menu_info

class ResturantMenuVoteSerializer(serializers.ModelSerializer):
    resturant_menu_item = ResturantMenuItemSerializer(many=True)
    resturant = ResturantSerializer(read_only=True)
    class Meta:
        model = ResturantMenu
        fields = ["id","resturant","name","description","status","menu_date","resturant_menu_item"] 
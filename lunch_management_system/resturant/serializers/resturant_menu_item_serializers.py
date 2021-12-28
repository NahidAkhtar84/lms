from rest_framework import serializers
from resturant.models.resturant_menu_item import ResturantMenuItem

class ResturantMenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResturantMenuItem
        fields = ["id","name","description"]
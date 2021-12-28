from rest_framework import serializers
from resturant.models.resturant import Resturant
from resturant.serializers.resturant_menu_serializers import ResturantMenuSerializer


class ResturantListForVoteSerializer(serializers.ModelSerializer):
    resturant_menus = ResturantMenuSerializer(many=True)
    class Meta:
        model = Resturant
        fields = ['name','resturant_menus']
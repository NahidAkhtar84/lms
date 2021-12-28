from rest_framework import serializers
from resturant.models.champion_resturant import ChampionResturant

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionResturant
        fields = ["resturant"]
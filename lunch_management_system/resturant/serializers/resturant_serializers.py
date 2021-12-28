from rest_framework import serializers
from resturant.models.resturant import Resturant

class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = ["id","name","description","status"]

class ChampionResturantSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField('_vote_count')

    def _vote_count(self, obj):
        vote_count = self.context.get("vote_count")
        if vote_count:
            return vote_count
        return False

    class Meta:
        model = Resturant
        fields = ["id","name","description","status", "vote_count"]

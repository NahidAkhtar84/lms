from rest_framework import serializers
from employee.models.vote import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["employee","resturant","vote", "voting_date"]


class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["resturant","vote"]
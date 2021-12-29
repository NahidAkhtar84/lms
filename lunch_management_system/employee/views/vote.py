from datetime import date

from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY
from drf_yasg.utils import swagger_auto_schema

from employee.models.vote import Vote
from employee.serializers.vote_serializers import VoteCreateSerializer, VoteSerializer
 

class VoteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=VoteCreateSerializer,
        responses={
            '201': 'CREATED Request',
            '400': "Bad Request"
        },
        security=[],
        operation_id='Create vote',
        operation_description='Create of vote',
    )
    def post(self, request, format=None):
        vote_data = request.data
        current_user = request.user

        if current_user.is_superuser == False:
            try:
                vote_exist = Vote.objects.get(employee=current_user, vote=True, voting_date=date.today())
            except:
                vote_exist = None

            if vote_exist is None:
                serializer = VoteCreateSerializer(data=vote_data)

                if serializer.is_valid():
                    serializer.save(employee=current_user, created_by=request.user, updated_by=request.user)

                else:
                    return Response({"detail": "Voting is not accomplished, Please try again!"}, status=status.HTTP_400_BAD_REQUEST)
                    
                return Response({"data": serializer.data, "detail": "Voted successfully!"},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "You have voted already, for today!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "You dont have privilege to vote!"}, status=status.HTTP_400_BAD_REQUEST)
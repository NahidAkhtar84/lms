from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import APIView

from employee.models.user import User
from employee.serializers.employee_serializers import EmployeeCreateSerializer, EmployeeSerializer, EmployeeEditSerializer
 

class EmployeeAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                user = User.objects.get(id=pk)
            except:
                return Response({"message": "Invaild users"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = EmployeeSerializer(user)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        user = User.objects.filter(is_superuser=False).order_by('-id')
        serializer = EmployeeSerializer(user, many=True)
    
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, format=None):

        user_data = request.data

        serializer = EmployeeCreateSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
        else:
           detail={"detail": serializer.errors}
           return Response(detail, status=status.HTTP_400_BAD_REQUEST)
            
        response_serializer = EmployeeSerializer(user_data)

           
        return Response({"data": response_serializer.data, "detail": "Employee has been successfully created."},
                        status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        if pk is not None:

            try:
                user_obj = User.objects.get(id=pk, is_superuser=False)
            except:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


            serializer = EmployeeEditSerializer(user_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

            else:
                return Response({"message": "Employee could not updated"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"data": serializer.data, "detail": "Employee has been successfully updated."},
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None, format=None):
        try:
            user_obj = User.objects.get(id=pk, is_superuser=False)
        except:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user_obj.delete()

        return Response({"message": "Data has been deleted!"}, status=status.HTTP_200_OK)
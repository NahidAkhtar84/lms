from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","email","first_name","last_name", "username"]


class EmployeeCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email address already exists")
        return lower_email

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    class Meta:
        model = User
        fields = ["email","first_name", "last_name", "username", "password"]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EmployeeEditSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    class Meta:
        model = User
        fields = ["first_name","last_name","username", "password"]

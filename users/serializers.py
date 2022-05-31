from rest_framework import serializers

from users.models import User


class RelatesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "avatar", "superhost")


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "avatar", "superhost", "favs")


class WriteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    # def validated_data(self, value):
    #     print(value)
    #     return value.upper()
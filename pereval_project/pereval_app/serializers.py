from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "surname", "phone", "name", "last_name"]

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.phone = validated_data.get('phone', instance.phone)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.name = validated_data.get('name', instance.name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.save()
            return instance


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['id', 'latitude', 'longitude', 'height']

        def create(self, validated_data):
            return Coord.objects.create(**validated_data)


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'level_winter', 'level_summer',
                  'level_autumn', 'level_spring', 'coordinations', 'photo']

    def create(self, validated_data):
        return Pereval.objects.create(**validated_data)

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'date_added',
            'title',
            'img',
            'pereval',
        ]

        def create(self, validated_data):
            return Image.objects.create(**validated_data)

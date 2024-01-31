from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "surname", "phone", "name", "last_name"]


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'data', 'title']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['id', 'pereval', 'latitude', 'longitude', 'height']


class PerevalSerializer(serializers.ModelSerializer):
    coordinations = CoordSerializer(many=True)
    photo = PhotoSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'level_winter', 'level_summer',
                  'level_autumn', 'level_spring', 'coordinations', 'photo']

    def create(self, validated_data):
        pereval = Pereval.objects.create(**validated_data)
        coordinations_data = validated_data.pop('coordinations')
        photo_data = validated_data.pop('photo')
        Coord.objects.create(pereval=pereval, **coordinations_data)
        for photo_data in photo_data:
            photo = Image.objects.create(**photo_data)
            PerevalImage.objects.create(foto=photo, pereval=pereval)
        return pereval
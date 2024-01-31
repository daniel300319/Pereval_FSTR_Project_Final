from rest_framework import serializers

from .models import Pereval


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('beauty_title',
                  'title',
                  'other_titles',
                  'coord',
                  'level_winter',
                  'level_spring',
                  'level_summer',
                  'level_autumn')
from rest_framework import serializers
from .models import Course, Price


class CoursesListSerializer(serializers.ModelSerializer):

    level_name = serializers.ReadOnlyField(source='level.name')

    class Meta:
        model = Course
        fields = ('id', 'name', 'level_name',
                  'headline', 'description', 'icon')


class PriceListSerializer(serializers.ModelSerializer):
    range = serializers.ReadOnlyField(source='age_range.range')
    features = serializers.StringRelatedField(many=True)

    class Meta:
        model = Price
        fields = ('id', 'name', 'amount', 'range', 'features')

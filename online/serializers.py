from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Price


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


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

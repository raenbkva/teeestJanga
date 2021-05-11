from rest_framework import serializers
from .models import *

class RecipesSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    get_ingredients = serializers.CharField()

    def get_ingredients(self,obj):
        return ",\n".join([i.title for i in obj.ingredient.all()])
    def create(self,validated_data):
        return Recipes.objects.create(**validated_data)

class DishesSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    manufacture_date = serializers.CharField()
    calories = serializers.CharField()
    sell_by = serializers.CharField()
    recipe = serializers.CharField()

    def create(self, validated_data):
        return Dishes.objects.create(**validated_data)
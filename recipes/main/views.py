from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import  *
from .serializers import *
# Create your views here.

def index(request):
    dishes = Dishes.objects.all()
    dishesPhoto = DishesPhoto.objects.all()
    return render(request, 'main/index.html', {'dishes':dishes,'photos':dishesPhoto})


class RecipesView(APIView):
    def get(self, request):
        RecipesApi = Recipes.objects.all()
        serializer = RecipesSerializer(RecipesApi, many=True)
        return Response({"Recipes": serializer.data})

    def post(self, request):
        RecipesApi = request.data.get('Recipes')
        serializer = RecipesSerializer(data=RecipesApi)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})


class DishesView(APIView):
    def get(self, request):
        DishesApi = Dishes.objects.all()
        serializer = DishesSerializer(DishesApi, many=True)
        return Response({"Dishes": serializer.data})

    def post(self, request):
        DishesApi = request.data.get('Dishes')
        serializer = DishesSerializer(data=DishesApi)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})
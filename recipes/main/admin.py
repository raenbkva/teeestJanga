from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
# Register your models here.

@admin.register(Recipes)
class RecipesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','title','description','get_ingredients',)
    search_fields = ['title','description']
    list_filter = ['title']
    def get_ingredients(self,obj):
        return ",\n".join([i.title for i in obj.ingredient.all()])
    def get_ordering(self,request):
        return [Lower('id')]
    get_ingredients.short_description = "Ингредиенты"
@admin.register(Ingredients)
class IngredientsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Следующие столбцы будут видны в админке
    list_display = ('id','title','manufacture_date','sell_by','calories','price')
    # Поиск по следующим полям
    search_fields = ['title','calories','price']
    # Фильтр по следующим полям
    list_filter = ['price','calories']
    # Добавляем в admin-actions следующие функции
    actions = ['price_50','price_100']
    # Сортировка по возрастанию по дефолту
    def get_ordering(self,request):
        return [Lower('id')]
    # Установить цену выбранных продуктов равно 50
    def price_50(self,request,queryset):
        queryset.update(price=50)
    # Установить цену выбранных продуктов равно 100
    def price_100(self,request,queryset):
        queryset.update(price=100)
    # Функция, ограничивающая форматы импорта файлов
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    # Функция, ограничивающая форматы экспорта файлов
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]
    price_50.short_description = 'Установить цену 50 рублей за кг'
    price_100.short_description = 'Установить цену 100 рублей за кг'

@admin.register(Manufacturers)
class ManufacturersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','company_name','ingredient')
    search_fields=['company_name','ingredient']
    list_filter = ['ingredient']
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]
@admin.register(Providers)
class ProvidersAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id','title','since','city')
    search_fields=['city','since','title']
    list_filter = ['city']
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]    

@admin.register(ProviderIngredients)
class ProviderIngredientsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('id','provider','ingredient')
    search_fields= ['provider__city','ingredient__title']
    list_filter= ['provider__city']
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()] 

@admin.register(Deliveries)
class DeliveriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id','date','ingredient','provider','city')
    search_fields = ['ingredient__title','provider__title','city']
    list_filter = ['ingredient__title','provider__title','city']
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(Dishes)
class DishesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','title','manufacture_date','sell_by','calories','recipe')
    search_fields = ['title','calories','recipe__title']
    list_filter = ['title','sell_by']
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(DishesPhoto)
class DishesPhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id','photo_url','dishe')
    search_fields = ['dishe']
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(News) 
class NewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id','title','description','date')
    list_filter = ['title','date']
    search_fields = ['title','description','date']
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(NewsPhotos)
class NewsPhotosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','news','photo_url')
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]
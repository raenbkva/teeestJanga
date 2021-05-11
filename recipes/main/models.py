from django.db import models

# Create your models here.

class Ingredients(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField('Название ингредиента')
    manufacture_date = models.DateField('Дата изготовлеиня')
    sell_by = models.DateField('Годен до')
    calories = models.IntegerField('Количество калорий')
    price = models.IntegerField("Цена за 1кг")

    class Meta:
        verbose_name = ('Ингредиент')
        verbose_name_plural = ('Ингредиенты')

    def __str__(self):
        return self.title

class Recipes(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField('Название рецепта')
    description = models.TextField('Описание рецепта')
    ingredient = models.ManyToManyField(Ingredients, verbose_name=("Ингредиенты"))

    class Meta:
        verbose_name = ('Рецепт')
        verbose_name_plural = ('Рецепты')
    

    def __str__(self):
        return str(self.title)
class Manufacturers(models.Model):

    id = models.AutoField(primary_key=True)
    company_name = models.TextField("Название производителя")
    ingredient = models.ForeignKey(Ingredients,related_name='Ингредиенты', verbose_name=("Производит"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ('Производитель')
        verbose_name_plural = ('Производители')
    def __str__(self):
        return self.company_name
class Providers(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField('Название поставщика')
    city = models.CharField(("Город откуда поставляют"), max_length=50)
    since = models.DateField('Дата основания')

    class Meta:
        verbose_name = ('Поставщик')
        verbose_name_plural = ('Поставщики')

    def __str__(self):
        return self.title

class ProviderIngredients(models.Model):

    id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Providers, verbose_name=("Поставщик"), on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, verbose_name=('Ингредиент'),on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Ингредиент поставщика")
        verbose_name_plural = ('Ингредиенты поставщиков')
    def __str__(self):
        return self.id
class Deliveries(models.Model):

    id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Providers, verbose_name=("Поставщик"), on_delete=models.CASCADE)
    date = models.DateField(("Дата поставки"), auto_now=False, auto_now_add=False)
    ingredient = models.ForeignKey(Ingredients, verbose_name=('Ингредиент'),on_delete=models.CASCADE)
    city = models.TextField('Город поставки')

    class Meta:
        verbose_name = ('Поставка')
        verbose_name_plural = ('Поставки')

    def __str__(self):
        return (self.ingredient.title + ' из ' + self.city)
class Dishes(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(("Название блюда"), max_length=50)
    manufacture_date = models.DateField('Дата изготовлеиня')
    calories = models.IntegerField('Количество калорий')
    sell_by = models.DateField('Годен до')
    recipe = models.ForeignKey(Recipes, verbose_name=('Рецепт'),on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Блюдо")
        verbose_name_plural = ("Блюда")

    def __str__(self):
        return (self.title)

class DishesPhoto(models.Model):

    id = models.AutoField(primary_key=True)
    photo_url = models.TextField('Ссылка на фотографию')
    dishe = models.ForeignKey(Dishes,related_name=('photos'),on_delete=models.CASCADE)

    class Meta:
        verbose_name=('Фото блюда')
        verbose_name_plural=('Фото блюд')
        
    def __str__(self):
        return (self.dishe.title)
class News(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField('Название новости')
    description = models.TextField('Текст новости')
    date = models.DateField('Дата публикации')

    class Meta:
        verbose_name=('Новость')
        verbose_name_plural=('Новости')
    def __str__(self):
        return (self.title)
class NewsPhotos(models.Model):

    id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, verbose_name=("Новость"), on_delete=models.CASCADE)
    photo_url = models.TextField('Ссылка на фотографию')

    class Meta:
        verbose_name = ('Фотография к новости')
        verbose_name_plural = ('Фотографии к новостям')
    def __str__(self):
        return (self.news.title)
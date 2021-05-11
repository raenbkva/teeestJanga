# Generated by Django 3.2.2 on 2021-05-06 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210506_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishes',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AddField(
            model_name='dishes',
            name='calories',
            field=models.IntegerField(default=1, verbose_name='Количество калорий'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DishesPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_url', models.TextField(verbose_name='Ссылка на фотографию')),
                ('dishe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dishes', verbose_name='Блюдо')),
            ],
        ),
    ]
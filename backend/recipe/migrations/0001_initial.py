# Generated by Django 5.0.2 on 2024-02-26 23:07

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('short_description', models.TextField(max_length=500, verbose_name='Краткое описание')),
                ('time', models.TextField(max_length=50, verbose_name='Время готовки')),
                ('ingredients', models.TextField(max_length=500, verbose_name='Ингридиенты')),
                ('description', models.TextField()),
                ('steps', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('thumbnail', models.ImageField(blank=True, upload_to='images/thumbnails/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Превью поста')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.categories', verbose_name='Катигория')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='recipe_reci_time_cr_a86743_idx')],
            },
        ),
    ]
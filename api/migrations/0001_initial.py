# Generated by Django 4.2.1 on 2023-05-29 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('discount_percentage', models.FloatField()),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('color', models.CharField(max_length=100)),
                ('main_image', models.ImageField(upload_to='product_images')),
                ('image1', models.ImageField(blank=True, upload_to='product_images')),
                ('image2', models.ImageField(blank=True, upload_to='product_images')),
                ('image3', models.ImageField(blank=True, upload_to='product_images')),
                ('image4', models.ImageField(blank=True, upload_to='product_images')),
                ('image5', models.ImageField(blank=True, upload_to='product_images')),
                ('image6', models.ImageField(blank=True, upload_to='product_images')),
                ('image7', models.ImageField(blank=True, upload_to='product_images')),
                ('image8', models.ImageField(blank=True, upload_to='product_images')),
                ('image9', models.ImageField(blank=True, upload_to='product_images')),
                ('image10', models.ImageField(blank=True, upload_to='product_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shopping Like',
                'verbose_name_plural': 'Shopping Likes',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shopping Card',
                'verbose_name_plural': 'Shopping Cards',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='api_categor_name_53a3ad_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['title', 'price'], name='api_product_title_be99e5_idx'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("product_img", models.ImageField(default=None, null=True, upload_to="product/img/thumbnail")),
                ("description_img", models.ImageField(default=None, null=True, upload_to="product/img/description")),
                ("description_text", models.TextField(default=None)),
                ("price", models.IntegerField(default=0)),
                ("travel_period", models.IntegerField(default=0)),
                ("discount", models.IntegerField(default=0)),
                ("view_count", models.IntegerField(default=0)),
                ("status", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

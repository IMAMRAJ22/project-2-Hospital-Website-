# Generated by Django 5.0.7 on 2024-08-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctorinfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Dc_img", models.ImageField(upload_to="Doctor/")),
                ("Dc_name", models.CharField(max_length=50)),
                ("Dc_sepc", models.CharField(max_length=50)),
            ],
        ),
    ]

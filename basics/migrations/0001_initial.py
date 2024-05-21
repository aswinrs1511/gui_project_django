# Generated by Django 4.2.13 on 2024-05-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentDepartment",
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
                ("DEPT_NAME", models.CharField(max_length=500)),
                ("DEPT_DESC", models.CharField(max_length=500)),
            ],
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('path', models.ImageField(upload_to='images/')),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]

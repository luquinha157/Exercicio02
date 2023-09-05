from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome_produto = models.CharField(max_length=200)
    description =  models.TextField()
    path = models.ImageField(upload_to="images/")
    preco = models.DecimalField(default=000.00, max_digits= 5, decimal_places=2)
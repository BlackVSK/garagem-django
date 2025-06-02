from django.db import models
from django.core.exceptions import ValidationError  ##Validation erro mostra o erro na interface administrativa
from django.core.validators import MinValueValidator

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome.upper()

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Acessório"
        verbose_name_plural="Acessórios"

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Cor"
        verbose_name_plural="Cores"

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0, validators=[MinValueValidator(0)])
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos", blank=True, null=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos", blank=True, null=True)
    Cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos", blank=True, null=True)
    acessorio= models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.Marca}, {self.Categoria}, {self.ano}, {self.Cor}"

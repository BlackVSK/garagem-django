# Generated by Django 5.2.1 on 2025-06-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_alter_veiculo_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='acessorio',
            field=models.ManyToManyField(related_name='veiculos', to='garagem.acessorio'),
        ),
    ]

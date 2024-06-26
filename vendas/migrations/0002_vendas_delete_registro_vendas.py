# Generated by Django 5.0.4 on 2024-04-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendas",
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
                (
                    "nome_cliente",
                    models.CharField(max_length=255, verbose_name="Nome do Cliente"),
                ),
                ("cpf_cliente", models.IntegerField(verbose_name="CPF do Cliente")),
                (
                    "telefone_cliente",
                    models.IntegerField(verbose_name="Telefone do Cliente"),
                ),
                (
                    "nome_produto",
                    models.CharField(max_length=255, verbose_name="Nome do Produto"),
                ),
                (
                    "preco_produto",
                    models.FloatField(max_length=10, verbose_name="Preço"),
                ),
                ("situação_produto", models.IntegerField(verbose_name="Situação")),
                ("observacao", models.TextField()),
                (
                    "data_venda",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de venda"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Registro_Vendas",
        ),
    ]

# Generated by Django 4.2.16 on 2024-10-27 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menus", "0001_initial"),
        ("eventos", "0002_remove_eventovenue_agregado_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
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
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("pendiente", "Pendiente"),
                            ("pagado", "Pagado"),
                            ("cancelado", "Cancelado"),
                        ],
                        max_length=20,
                    ),
                ),
                ("fecha_creacion", models.DateField(auto_now_add=True)),
                (
                    "evento",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventos.evento",
                    ),
                ),
                (
                    "items_pedido",
                    models.ManyToManyField(blank=True, null=True, to="menus.menuitem"),
                ),
            ],
        ),
    ]

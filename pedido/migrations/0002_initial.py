# Generated by Django 4.2.16 on 2024-10-27 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("promociones", "0001_initial"),
        ("comercios", "0004_alter_venue_actividades"),
        ("usuarios", "0004_login_usuario_actividades_spontime_activo_and_more"),
        ("pedido", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="items_promocion",
            field=models.ManyToManyField(
                blank=True, null=True, to="promociones.promocion"
            ),
        ),
        migrations.AddField(
            model_name="pedido",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="usuarios.usuario"
            ),
        ),
        migrations.AddField(
            model_name="pedido",
            name="venue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="comercios.venue"
            ),
        ),
    ]

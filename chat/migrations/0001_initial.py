# Generated by Django 4.2.16 on 2024-10-27 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("grupos", "0002_remove_calificaciongrupo_fecha_remove_grupo_fecha_and_more"),
        ("usuarios", "0004_login_usuario_actividades_spontime_activo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mensaje",
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
                ("contenido", models.TextField()),
                ("fecha_envio", models.DateTimeField(auto_now_add=True)),
                (
                    "grupo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mensajes",
                        to="grupos.grupo",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.usuario",
                    ),
                ),
            ],
        ),
    ]

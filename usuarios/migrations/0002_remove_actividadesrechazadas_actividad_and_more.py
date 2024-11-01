# Generated by Django 4.2.16 on 2024-10-26 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("actividades", "0001_initial"),
        ("comercios", "0004_alter_venue_actividades"),
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actividadesrechazadas",
            name="actividad",
        ),
        migrations.RemoveField(
            model_name="actividadesrechazadas",
            name="usuario",
        ),
        migrations.RemoveField(
            model_name="calificaciongrupo",
            name="grupo",
        ),
        migrations.RemoveField(
            model_name="calificaciongrupo",
            name="usuario",
        ),
        migrations.RemoveField(
            model_name="grupo",
            name="actividad",
        ),
        migrations.RemoveField(
            model_name="grupo",
            name="usuarios",
        ),
        migrations.AlterField(
            model_name="calificacionactividad",
            name="actividad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calificaciones_usuario",
                to="actividades.actividad",
            ),
        ),
        migrations.AlterField(
            model_name="calificacionactividad",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calificaciones_usuario_usuarios",
                to="usuarios.usuario",
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="actividades_no_me_gustan",
            field=models.ManyToManyField(
                related_name="usuarios_no_gustan", to="actividades.actividad"
            ),
        ),
        migrations.DeleteModel(
            name="Actividad",
        ),
        migrations.DeleteModel(
            name="ActividadesRechazadas",
        ),
        migrations.DeleteModel(
            name="CalificacionGrupo",
        ),
        migrations.DeleteModel(
            name="Grupo",
        ),
    ]

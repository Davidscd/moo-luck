import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animales', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoSanitario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('medicamento', models.CharField(blank=True, max_length=100, null=True)),
                ('dosis', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateField()),
                ('proxima_fecha', models.DateField(blank=True, null=True)),
                ('animal', models.ForeignKey(db_column='animal_id', on_delete=django.db.models.deletion.CASCADE, related_name='eventos_sanitarios', to='animales.animal')),
                ('veterinario', models.ForeignKey(blank=True, db_column='veterinario_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'eventos_sanitarios',
                'ordering': ['-fecha'],
            },
        ),
    ]

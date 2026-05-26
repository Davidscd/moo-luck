import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fincas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('raza', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('macho', 'Macho'), ('hembra', 'Hembra')], max_length=20, null=True)),
                ('proposito', models.CharField(blank=True, choices=[('leche', 'Leche'), ('carne', 'Carne'), ('doble_proposito', 'Doble Propósito')], max_length=50, null=True)),
                ('estado', models.CharField(blank=True, choices=[('activo', 'Activo'), ('vendido', 'Vendido'), ('muerto', 'Muerto'), ('gestante', 'Gestante'), ('seco', 'Seco')], max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('peso_inicial', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finca', models.ForeignKey(blank=True, db_column='finca_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animales', to='fincas.finca')),
                ('madre', models.ForeignKey(blank=True, db_column='madre_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hijos_madre', to='animales.animal')),
                ('padre', models.ForeignKey(blank=True, db_column='padre_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hijos_padre', to='animales.animal')),
            ],
            options={
                'db_table': 'animales',
                'ordering': ['codigo'],
            },
        ),
    ]

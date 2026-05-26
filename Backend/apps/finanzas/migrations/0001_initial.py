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
            name='CategoriaGasto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(blank=True, choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')], max_length=50, null=True)),
                ('icono', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'categorias_gasto',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')], max_length=50)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('comprobante_url', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(blank=True, db_column='categoria_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transacciones', to='finanzas.categoriagasto')),
                ('finca', models.ForeignKey(db_column='finca_id', on_delete=django.db.models.deletion.CASCADE, related_name='transacciones', to='fincas.finca')),
            ],
            options={
                'db_table': 'transacciones',
                'ordering': ['-fecha'],
            },
        ),
    ]

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
            name='Produccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('litros_manana', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('litros_tarde', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('litros_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('animal', models.ForeignKey(db_column='animal_id', on_delete=django.db.models.deletion.CASCADE, related_name='producciones', to='animales.animal')),
                ('registrado_por', models.ForeignKey(blank=True, db_column='registrado_por', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'producciones',
                'ordering': ['-fecha'],
            },
        ),
    ]

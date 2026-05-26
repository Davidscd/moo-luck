import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_parto', models.DateField()),
                ('tipo_parto', models.CharField(blank=True, choices=[('normal', 'Normal'), ('distocico', 'Distócico'), ('cesarea', 'Cesárea')], max_length=50, null=True)),
                ('numero_crias', models.IntegerField(blank=True, null=True)),
                ('estado_cria', models.CharField(blank=True, choices=[('vivo', 'Vivo'), ('muerto', 'Muerto'), ('aborto', 'Aborto')], max_length=100, null=True)),
                ('madre', models.ForeignKey(db_column='madre_id', on_delete=django.db.models.deletion.CASCADE, related_name='partos', to='animales.animal')),
            ],
            options={
                'db_table': 'partos',
                'ordering': ['-fecha_parto'],
            },
        ),
    ]

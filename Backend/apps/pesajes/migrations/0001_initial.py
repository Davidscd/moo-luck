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
            name='Pesaje',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('peso_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateField()),
                ('metodo', models.CharField(blank=True, max_length=100, null=True)),
                ('animal', models.ForeignKey(db_column='animal_id', on_delete=django.db.models.deletion.CASCADE, related_name='pesajes', to='animales.animal')),
            ],
            options={
                'db_table': 'pesajes',
                'ordering': ['-fecha'],
            },
        ),
    ]

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
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password_hash', models.TextField()),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('veterinario', 'Veterinario'), ('operario', 'Operario'), ('propietario', 'Propietario')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finca', models.ForeignKey(blank=True, db_column='finca_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='fincas.finca')),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ['nombre'],
            },
        ),
    ]

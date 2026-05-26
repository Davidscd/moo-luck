import uuid
from django.db import models


class Usuario(models.Model):
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('veterinario', 'Veterinario'),
        ('operario', 'Operario'),
        ('propietario', 'Propietario'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password_hash = models.TextField()
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    finca = models.ForeignKey(
        'fincas.Finca',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='usuarios',
        db_column='finca_id'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.rol})"

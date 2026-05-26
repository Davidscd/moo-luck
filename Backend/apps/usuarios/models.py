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

    @property
    def is_authenticated(self):
        return True


class AuthToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='tokens',
        db_column='usuario_id',
    )
    key_hash = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'auth_tokens'
        ordering = ['-created_at']

    def __str__(self):
        return f"Token de {self.usuario.email}"

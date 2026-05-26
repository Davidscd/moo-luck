import uuid
from django.db import models


class Animal(models.Model):
    SEXO_CHOICES = [('macho', 'Macho'), ('hembra', 'Hembra')]
    PROPOSITO_CHOICES = [('leche', 'Leche'), ('carne', 'Carne'), ('doble_proposito', 'Doble Propósito')]
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('vendido', 'Vendido'),
        ('muerto', 'Muerto'),
        ('gestante', 'Gestante'),
        ('seco', 'Seco'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES, blank=True, null=True)
    proposito = models.CharField(max_length=50, choices=PROPOSITO_CHOICES, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    peso_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    madre = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='hijos_madre', db_column='madre_id'
    )
    padre = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='hijos_padre', db_column='padre_id'
    )
    finca = models.ForeignKey(
        'fincas.Finca', on_delete=models.CASCADE,
        null=True, blank=True, related_name='animales', db_column='finca_id'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'animales'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nombre or 'Sin nombre'}"

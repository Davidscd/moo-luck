import uuid
from django.db import models


class CategoriaGasto(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, blank=True, null=True)
    icono = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'categorias_gasto'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    finca = models.ForeignKey(
        'fincas.Finca', on_delete=models.CASCADE,
        related_name='transacciones', db_column='finca_id'
    )
    categoria = models.ForeignKey(
        CategoriaGasto, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='transacciones', db_column='categoria_id'
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    comprobante_url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'transacciones'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.tipo} - ${self.monto} - {self.fecha}"

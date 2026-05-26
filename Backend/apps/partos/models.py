import uuid
from django.db import models


class Parto(models.Model):
    TIPO_PARTO_CHOICES = [
        ('normal', 'Normal'),
        ('distocico', 'Distócico'),
        ('cesarea', 'Cesárea'),
    ]
    ESTADO_CRIA_CHOICES = [
        ('vivo', 'Vivo'),
        ('muerto', 'Muerto'),
        ('aborto', 'Aborto'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    madre = models.ForeignKey(
        'animales.Animal', on_delete=models.CASCADE,
        related_name='partos', db_column='madre_id'
    )
    fecha_parto = models.DateField()
    tipo_parto = models.CharField(max_length=50, choices=TIPO_PARTO_CHOICES, blank=True, null=True)
    numero_crias = models.IntegerField(blank=True, null=True)
    estado_cria = models.CharField(max_length=100, choices=ESTADO_CRIA_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'partos'
        ordering = ['-fecha_parto']

    def __str__(self):
        return f"Parto de {self.madre.codigo} - {self.fecha_parto}"

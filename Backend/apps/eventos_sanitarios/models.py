import uuid
from django.db import models


class EventoSanitario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(
        'animales.Animal', on_delete=models.CASCADE,
        related_name='eventos_sanitarios', db_column='animal_id'
    )
    tipo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    medicamento = models.CharField(max_length=100, blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField()
    proxima_fecha = models.DateField(blank=True, null=True)
    veterinario = models.ForeignKey(
        'usuarios.Usuario', on_delete=models.SET_NULL,
        null=True, blank=True, db_column='veterinario_id'
    )

    class Meta:
        db_table = 'eventos_sanitarios'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.tipo} - {self.animal.codigo} - {self.fecha}"

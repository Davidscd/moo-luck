import uuid
from django.db import models


class Produccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(
        'animales.Animal', on_delete=models.CASCADE,
        related_name='producciones', db_column='animal_id'
    )
    litros_manana = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    litros_tarde = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    litros_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    registrado_por = models.ForeignKey(
        'usuarios.Usuario', on_delete=models.SET_NULL,
        null=True, blank=True, db_column='registrado_por'
    )

    class Meta:
        db_table = 'producciones'
        ordering = ['-fecha']

    def save(self, *args, **kwargs):
        # Auto-calcular total
        self.litros_total = (self.litros_manana or 0) + (self.litros_tarde or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.animal.codigo} - {self.fecha} - {self.litros_total}L"

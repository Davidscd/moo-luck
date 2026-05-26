import uuid
from django.db import models


class Pesaje(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(
        'animales.Animal', on_delete=models.CASCADE,
        related_name='pesajes', db_column='animal_id'
    )
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField()
    metodo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'pesajes'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.animal.codigo} - {self.peso_kg}kg - {self.fecha}"

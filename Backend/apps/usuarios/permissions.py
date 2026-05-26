from rest_framework.exceptions import PermissionDenied, ValidationError


def is_admin(user):
    return getattr(user, 'rol', None) == 'admin'


def owned_farm_ids(user):
    from apps.fincas.models import Finca

    if not getattr(user, 'id', None):
        return Finca.objects.none().values_list('id', flat=True)
    if is_admin(user):
        return Finca.objects.values_list('id', flat=True)
    return Finca.objects.filter(propietario_id=user.id).values_list('id', flat=True)


def ensure_owned_farm(user, finca_id):
    if not finca_id:
        raise ValidationError({'finca': 'Selecciona una finca.'})
    if is_admin(user):
        return
    if str(finca_id) not in {str(item) for item in owned_farm_ids(user)}:
        raise PermissionDenied('No tienes acceso a esta finca.')


def ensure_owned_animal(user, animal_id):
    from apps.animales.models import Animal

    if not animal_id:
        raise ValidationError({'animal': 'Selecciona un animal.'})
    if is_admin(user):
        return
    exists = Animal.objects.filter(id=animal_id, finca_id__in=owned_farm_ids(user)).exists()
    if not exists:
        raise PermissionDenied('No tienes acceso a este animal.')

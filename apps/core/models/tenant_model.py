import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tenant(models.Model):
    tenant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant_name = models.CharField(max_length=255, help_text="Nombre completo de la empresa/organización")
    tenant_code = models.CharField(max_length=50, unique=True, help_text="Código corto o acrónimo para la empresa")
    contact_name = models.CharField(max_length=255, help_text="Nombre de la persona de contacto principal")
    contact_email = models.EmailField(max_length=255, help_text="Correo electrónico de contacto")
    contact_phone = models.CharField(max_length=50, blank=True, null=True, help_text="Teléfono de contacto principal")
    address_line1 = models.CharField(max_length=255, help_text="Dirección principal (calle, número, etc.)")
    address_line2 = models.CharField(max_length=255, blank=True, null=True, help_text="Complemento de dirección (opcional)")
    city = models.CharField(max_length=100, help_text="Ciudad")
    state = models.CharField(max_length=100, help_text="Estado o provincia")
    country = models.CharField(max_length=100, help_text="País")
    postal_code = models.CharField(max_length=20, help_text="Código postal")
    domain = models.CharField(max_length=255, blank=True, null=True, help_text="Dominio o subdominio personalizado")
    is_active = models.BooleanField(default=True, help_text="Estado del tenant (activo=True, inactivo=False)")
    subscription_plan = models.CharField(max_length=50, blank=True, null=True, help_text="Plan o tipo de servicio contratado")
    SUBSCRIPTION_STATUS_CHOICES = [
        ('active', 'Activo'),
        ('expired', 'Expirado'),
        ('cancelled', 'Cancelado'),
        ('trial', 'Prueba'),
    ]
    subscription_status = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_STATUS_CHOICES,
        default='active',
        help_text="Estado de la suscripción"
    )
    start_date = models.DateTimeField(blank=True, null=True, help_text="Fecha de inicio del servicio")
    end_date = models.DateTimeField(blank=True, null=True, help_text="Fecha de expiración del servicio")
    metadata = models.JSONField(blank=True, null=True, help_text="Información adicional en formato JSON")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del registro")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha de última actualización del registro")
    created_by = models.ForeignKey(User, related_name='tenants_created', on_delete=models.SET_NULL, blank=True, null=True, help_text="Usuario que creó el registro")
    updated_by = models.ForeignKey(User, related_name='tenants_updated', on_delete=models.SET_NULL, blank=True, null=True, help_text="Usuario que actualizó el registro")

    def __str__(self):
        return self.tenant_name



import uuid

from django.db import models


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
    subscription_status = models.BooleanField(default=True, help_text="Estado de la suscripción (activo=True, expirado=False)")
    start_date = models.DateTimeField(blank=True, null=True, help_text="Fecha de inicio del servicio")
    end_date = models.DateTimeField(blank=True, null=True, help_text="Fecha de expiración del servicio")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del registro")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha de última actualización del registro")
    
    def __str__(self):
        return self.tenant_name

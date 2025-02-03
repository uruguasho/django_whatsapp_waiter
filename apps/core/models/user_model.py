import uuid
from django.db import models
from .tenant_model import Tenant


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenants = models.ManyToManyField(Tenant, related_name='users')
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, help_text="Rol del usuario (cliente, agente, admin)")
    is_active = models.BooleanField(default=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
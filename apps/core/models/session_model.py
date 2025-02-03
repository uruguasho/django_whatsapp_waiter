import uuid
from django.db import models
from .tenant_model import Tenant
from .user_model import User
from .order_model import Order

import uuid
from django.db import models
from .tenant_model import Tenant
from .user_model import User
from .order_model import Order

class Session(models.Model):
    SESSION_STATUS_CHOICES = [
        ('active', 'Activo'),
        ('pending', 'Pendiente'),
        ('closed', 'Cerrado'),
        ('expired', 'Expirado'),
        ('on_hold', 'En espera'),
    ]

    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='sessions')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')
    status = models.CharField(
        max_length=20,
        choices=SESSION_STATUS_CHOICES,
        default='pending',
        help_text="Estado de la sesión"
    )
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Session {self.session_id} - {self.get_status_display()}"

import uuid
from django.db import models
from .order_model import Order


import uuid
from django.db import models
from .order_model import Order

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
        ('failed', 'Fallido'),
        ('refunded', 'Reembolsado'),
        ('cancelled', 'Cancelado'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Tarjeta de crédito'),
        ('debit_card', 'Tarjeta de débito'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Transferencia bancaria'),
        ('cash', 'Efectivo'),
        ('crypto', 'Criptomoneda'),
    ]

    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
        help_text="Estado del pago"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
        help_text="Método de pago utilizado"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Pago {self.payment_id} - {self.amount} ({self.get_status_display()})"

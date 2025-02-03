import uuid
from django.db import models
from .tenant_model import Tenant
from .product_model import Product, Extra

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=255, help_text="Nombre del cliente")
    customer_phone = models.CharField(max_length=50, help_text="Teléfono del cliente")
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pendiente'),
        ('processing', 'En proceso'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado')
    ], default='pending', help_text="Estado del pedido")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio total del pedido")
    notes = models.TextField(blank=True, null=True, help_text="Notas adicionales para el pedido")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.order_id} - {self.customer_name}"

class OrderItem(models.Model):
    order_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1, help_text="Cantidad del producto")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio unitario del producto")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio total del ítem")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} en pedido {self.order.order_id}"

class OrderItemExtra(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_item_extras')
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE, related_name='order_item_extras')
    quantity = models.PositiveIntegerField(default=1, help_text="Cantidad del extra")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del extra")

    class Meta:
        unique_together = ('order_item', 'extra')

    def __str__(self):
        return f"{self.quantity} x {self.extra.name} para {self.order_item.product.name}"

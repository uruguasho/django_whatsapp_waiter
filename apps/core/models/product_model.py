import uuid
from django.db import models
from .tenant_model import Tenant

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255, help_text="Nombre de la categoría")
    description = models.TextField(blank=True, null=True, help_text="Descripción de la categoría")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=255, help_text="Nombre del producto")
    description = models.TextField(blank=True, null=True, help_text="Descripción del producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del producto")
    ingredients = models.TextField(blank=True, null=True, help_text="Ingredientes del producto")
    allergens = models.TextField(blank=True, null=True, help_text="Alérgenos del producto")
    is_active = models.BooleanField(default=True, help_text="Indica si el producto está activo")
    metadata = models.JSONField(blank=True, null=True, help_text="Información adicional en formato JSON")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Extra(models.Model):
    extra_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='extras')
    name = models.CharField(max_length=255, help_text="Nombre del extra")
    description = models.TextField(blank=True, null=True, help_text="Descripción del extra")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del extra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductExtra(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_extras')
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE, related_name='product_extras')
    is_required = models.BooleanField(default=False, help_text="Indica si el extra es obligatorio para el producto")

    class Meta:
        unique_together = ('product', 'extra')

    def __str__(self):
        return f"{self.product.name} - {self.extra.name}"

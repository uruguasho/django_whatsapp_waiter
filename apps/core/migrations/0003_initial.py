# Generated by Django 5.1.5 on 2025-02-02 23:45

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_tenant'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre de la categoría', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Descripción de la categoría', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('message_type', models.CharField(help_text='Tipo de mensaje (texto, imagen, etc.)', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('metadata', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(help_text='Nombre del cliente', max_length=255)),
                ('customer_phone', models.CharField(help_text='Teléfono del cliente', max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('processing', 'En proceso'), ('completed', 'Completado'), ('cancelled', 'Cancelado')], default='pending', help_text='Estado del pedido', max_length=50)),
                ('total_price', models.DecimalField(decimal_places=2, help_text='Precio total del pedido', max_digits=10)),
                ('notes', models.TextField(blank=True, help_text='Notas adicionales para el pedido', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageProcessed',
            fields=[
                ('processed_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='processed', to='core.message')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('completed', 'Completado'), ('failed', 'Fallido'), ('refunded', 'Reembolsado'), ('cancelled', 'Cancelado')], default='pending', help_text='Estado del pago', max_length=20)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Tarjeta de crédito'), ('debit_card', 'Tarjeta de débito'), ('paypal', 'PayPal'), ('bank_transfer', 'Transferencia bancaria'), ('cash', 'Efectivo'), ('crypto', 'Criptomoneda')], default='cash', help_text='Método de pago utilizado', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre del producto', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Descripción del producto', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Precio del producto', max_digits=10)),
                ('ingredients', models.TextField(blank=True, help_text='Ingredientes del producto', null=True)),
                ('allergens', models.TextField(blank=True, help_text='Alérgenos del producto', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Indica si el producto está activo')),
                ('metadata', models.JSONField(blank=True, help_text='Información adicional en formato JSON', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Cantidad del producto')),
                ('unit_price', models.DecimalField(decimal_places=2, help_text='Precio unitario del producto', max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, help_text='Precio total del ítem', max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='core.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Activo'), ('pending', 'Pendiente'), ('closed', 'Cerrado'), ('expired', 'Expirado'), ('on_hold', 'En espera')], default='pending', help_text='Estado de la sesión', max_length=20)),
                ('opened_at', models.DateTimeField(auto_now_add=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='core.order')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.session'),
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('tenant_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tenant_name', models.CharField(help_text='Nombre completo de la empresa/organización', max_length=255)),
                ('tenant_code', models.CharField(help_text='Código corto o acrónimo para la empresa', max_length=50, unique=True)),
                ('contact_name', models.CharField(help_text='Nombre de la persona de contacto principal', max_length=255)),
                ('contact_email', models.EmailField(help_text='Correo electrónico de contacto', max_length=255)),
                ('contact_phone', models.CharField(blank=True, help_text='Teléfono de contacto principal', max_length=50, null=True)),
                ('address_line1', models.CharField(help_text='Dirección principal (calle, número, etc.)', max_length=255)),
                ('address_line2', models.CharField(blank=True, help_text='Complemento de dirección (opcional)', max_length=255, null=True)),
                ('city', models.CharField(help_text='Ciudad', max_length=100)),
                ('state', models.CharField(help_text='Estado o provincia', max_length=100)),
                ('country', models.CharField(help_text='País', max_length=100)),
                ('postal_code', models.CharField(help_text='Código postal', max_length=20)),
                ('domain', models.CharField(blank=True, help_text='Dominio o subdominio personalizado', max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Estado del tenant (activo=True, inactivo=False)')),
                ('subscription_plan', models.CharField(blank=True, help_text='Plan o tipo de servicio contratado', max_length=50, null=True)),
                ('subscription_status', models.CharField(choices=[('active', 'Activo'), ('expired', 'Expirado'), ('cancelled', 'Cancelado'), ('trial', 'Prueba')], default='active', help_text='Estado de la suscripción', max_length=20)),
                ('start_date', models.DateTimeField(blank=True, help_text='Fecha de inicio del servicio', null=True)),
                ('end_date', models.DateTimeField(blank=True, help_text='Fecha de expiración del servicio', null=True)),
                ('metadata', models.JSONField(blank=True, help_text='Información adicional en formato JSON', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de última actualización del registro')),
                ('created_by', models.ForeignKey(blank=True, help_text='Usuario que creó el registro', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenants_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='Usuario que actualizó el registro', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenants_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='core.tenant'),
        ),
        migrations.AddField(
            model_name='product',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.tenant'),
        ),
        migrations.AddField(
            model_name='order',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.tenant'),
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('extra_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre del extra', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Descripción del extra', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Precio del extra', max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='core.tenant')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='core.tenant'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('role', models.CharField(help_text='Rol del usuario (cliente, agente, admin)', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tenants', models.ManyToManyField(related_name='users', to='core.tenant')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='core.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to='core.user'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=255)),
                ('details', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.tenant')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Cantidad del extra')),
                ('price', models.DecimalField(decimal_places=2, help_text='Precio del extra', max_digits=10)),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_extras', to='core.extra')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_extras', to='core.orderitem')),
            ],
            options={
                'unique_together': {('order_item', 'extra')},
            },
        ),
        migrations.CreateModel(
            name='ProductExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(default=False, help_text='Indica si el extra es obligatorio para el producto')),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_extras', to='core.extra')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_extras', to='core.product')),
            ],
            options={
                'unique_together': {('product', 'extra')},
            },
        ),
    ]

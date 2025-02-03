import uuid
from django.db import models
from .message_model import Message

class MessageProcessed(models.Model):
    processed_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_id = models.CharField(max_length=255, unique=True)
    processed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.processed_id)
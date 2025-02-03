import uuid
from django.db import models
from .user_model import User
from .session_model import Session


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    content = models.TextField()
    message_type = models.CharField(max_length=50, help_text="Tipo de mensaje (texto, imagen, etc.)")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.content[:50]
from django.utils import timezone

from apps.core.models.message_processed import MessageProcessed


def extract_message_data(message_data):
    """Extraer los datos del mensaje."""
    return {
        'wa_message_id': message_data.get('id'),
        'from_number': message_data.get('from'),
        'timestamp': message_data.get('timestamp'),
        'text': message_data.get('text', {}).get('body'),
        'type': message_data.get('type'),
    }

def save_incoming_message(extracted_data):
    """Guardar el mensaje en la base de datos."""
    wa_message_id = extracted_data['wa_message_id']

    if MessageProcessed.objects.filter(message_id=wa_message_id).exists():
        return False 

    # Registrar en MessageProcessed
    message_obj = MessageProcessed.objects.create(
        message_id=wa_message_id,
        processed_at=timezone.now()
    )

    return True
import json

from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.core.models.message_processed import MessageProcessed
from apps.whatsapp.services import extract_message_data, save_incoming_message


VERIFY_TOKEN = 'R0m1n4'

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        
        else:
            return HttpResponse('Error de verificación', status=403)
        
    elif request.method == 'POST':
        data = json.loads(request.body)
        
        for entry in data.get('entry', []):
            
            for change in entry.get('changes', []):
                value = change.get('value', {})
                messages = value.get('messages', [])
                
                for message_data in messages:
                    # Extraer los datos del mensaje recibido
                    extracted_data = extract_message_data(message_data)

                    # Guardar el mensaje en la base de datos para evitar duplicados
                    was_processed = save_incoming_message(extracted_data)

                    if not was_processed:
                        print (f"❌ Mensaje duplicado: {extracted_data['wa_message_id']}")
                        return JsonResponse({'status': 'duplicado'}, status=200)
                    
                    print(f"✅ Mensaje guardado: {extracted_data['wa_message_id']}")

        return JsonResponse({'status': 'ok'}, status=200)
    
    return JsonResponse({'error': 'Método no permitido'}, status=400)


"""
Mensaje recibido:  {
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "551609014706842",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15551750561",
              "phone_number_id": "579482118572875"
            },
            "contacts": [
              {
                "profile": {
                  "name": "Uruguayo \ud83d\udc96"
                },
                "wa_id": "34607227417"
              }
            ],
            "messages": [
              {
                "from": "34607227417",
                "id": "wamid.HBgLMzQ2MDcyMjc0MTcVAgASGBQzQTkwQkE1MUQ2QjNFQ0E0MzlBOAA=",
                "timestamp": "1738543963",
                "text": {
                  "body": "Hola"
                },
                "type": "text"
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}
"""
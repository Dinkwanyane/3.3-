from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv


load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


@csrf_exempt
def bot(request):
    message = request.POST.get("Body", "").lower()

    response = MessagingResponse()

    if message == "hello":
        response.message("Hello! Welcome to our WhatsApp chatbot.")

    return HttpResponse(str(response), content_type="text/xml")




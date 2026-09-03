# 3.3-
# WhatsApp Chatbot

## Goal:
Build a simple WhatsApp chatbot using Django and Twilio.

##Technologies:

- Python
- Django
- Twilio
- WhatsApp
- ngrok
- Vscode
- Git and GitHub

## Project structure

- whatsappBot/
- ├── bot/
- │   ├── migrations/
- │   ├── __init__.py
- │   ├── admin.py
- │   ├── apps.py
- │   ├── models.py
- │   ├── tests.py
- │   ├── urls.py
- │   └── views.py
- ├── whatsappBot/
- │   ├── __init__.py
- │   ├── asgi.py
- │   ├── settings.py
- │   ├── urls.py
- │   └── wsgi.py
- ├── .gitignore
- ├── manage.py
- └── requirements.txt


## How the Chatbot Works

-1. The user sends a WhatsApp message.

-2. Twilio receives the message.

-3.  Twilio sends the message to the Django webhook.

-4.  Django reads:

-  Body - the message sent by the user.

-  ProfileName - the user's WhatsApp profile name.

-  From - the user's WhatsApp number.

-  5.   Django checks the message.

-6. If the message is "hi", the bot creates a personalised response.

-7. Twilio sends the response back to WhatsApp.

Example:

User: hi

Bot: Hi Mpho, how are you?

## Environment Variables

Twilio credentials should not be stored directly in views.py.

Never commit the Twilio Auth Token to GitHub

## Running the Project

- Activate the virtual environment:

use python 3.14 and run workon env_name

- Move to the Django project

- Start Django:

python manage.py runserver

In another terminal, start ngrok:

run ngrok http 8000

Copy the HTTPS ngrok address and use it as the Twilio webhook URL. Note that the exact ngrok address can change when a new ngrok session is started.

- Twilio Webhook

Twilio needs to know where to send incoming WhatsApp messages.

The webhook should point to the Django bot endpoint:

https://YOUR-NGROK-URL/bot/

The webhook method should be POST because the Django code reads the
incoming information from request.POST.

- Testing

Send this message from WhatsApp:

hi

Expected response:

Hi [your WhatsApp profile name], how are you?

Check the Django terminal to confirm that the request was received. It
can also be useful to print the incoming message, sender name, sender
number, and Twilio message SID.

## Troubleshooting

In case of a situation where troubleshooting is required, create a separate branch for troubleshooting so that code original code does not get broken. 

### Issues encountered
- After sending a hi text to the chatbot, did not receive a response. Discovered that the correct ContentSid was not used. Debugged and used the correct ContentSid and ran the Django project once more and received a response that was created by a template found on twilio. Twilio's current trial documentation says trial Messages API requests have restrictions and require a  using a Twilio-provided WhatsApp template ContentSid for outbound messages. The current twilo trial account system limits to using the provided whatsapp templates.  



# Imports the render function from Django.
# The render function is normally used to display an HTML template.
# It is not being used in this chatbot code, but it can be useful
# when creating web pages in Django.
from django.shortcuts import render

# Imports HttpResponse from Django.
# HttpResponse is used to send a simple response back to the browser
# or to the service that made the request
from django.http import HttpResponse

# Imports the Client class from the Twilio library.
# Client allows our Django application to communicate with Twilio's API.
# We use it to send WhatsApp messages through Twilio.
from twilio.rest import Client

# Imports the csrf_exempt decorator from Django.
# Django normally protects POST requests against CSRF attacks.
# Twilio sends the POST request to our webhook, so we use @csrf_exempt
# to allow Twilio's request to reach this function.
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# The Account SID identifies the Twilio account being used.
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXX'
# The Auth Token is used together with the Account SID to authenticate
# the application with Twilio.
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXX'

# Creates a Twilio Client object.
#
# Client is a class provided by the Twilio library.
# We give it the Account SID and Auth Token so that Twilio knows
# which account is making the API request and can authenticate it.
#
# After creating the client, we can use:
# client.messages.create(...)
#
# to send a WhatsApp message.
client = Client(account_sid, auth_token)

# A decorator changes or adds behaviour to a Python function.
# Here, it tells Django not to require a CSRF token for this particular
# view because the request is coming from Twilio rather than from a
# normal Django HTML form.
@csrf_exempt

#The bot() function is the main function that handles the
# incoming WhatsApp message.
#
# "request" contains information about the HTTP request sent
# to our Django application.
#
# When Twilio receives a WhatsApp message and sends it to our
# webhook, Django runs this function.
def bot(request):

# request.POST contains the data sent by Twilio in the POST request.
    #
    # ["Body"] gets the actual text message sent by the WhatsApp user.
    #
    # For example, if the user sends:
    #       Hello
    #
    # then incoming_message will contain:
    #       "Hello"    
    incoming_message = request.POST["Body"]

    # "ProfileName" contains the WhatsApp profile name of the person
    # who sent the message.
    #
    # This allows us to personalise the response.
    #
    # For example, if the user's WhatsApp profile name is Mpho,
    # sender_name will contain:
    #       "Mpho"
    sender_name = request.POST["ProfileName"]

    # "From" contains the WhatsApp number of the person who sent
    # the message.
    #
    # Twilio normally provides this in a format such as:
    #       whatsapp:+27XXXXXXXXX
    #
    # The value is stored in sender_number so that the application
    # knows where the message came from.
    sender_number = request.POST["From"]

 # client.messages.create() sends a message using Twilio.
    #
    # "client" was created earlier using the Twilio Account SID
    # and Auth Token.
    #
    # The messages.create() function sends the actual outgoing
    # WhatsApp message.
    outgoing_message = client.messages.create(

         # "from_" specifies the WhatsApp number that the message
        # is being sent FROM.
        from_='whatsapp:+17372508034',


        body='Hi {}, how are you?'.format(sender_name),

        # "content_sid" identifies a Twilio Content Template.
          # A ContentSid identifies a message template that has been
        # created in Twilio's Content Template Builder
        content_sid="XXXXXXXXXXXXXXXXXXXXXXX",

      

        # "to" specifies the WhatsApp number that should receive
        # the outgoing message.
        to='whatsapp:+27723784240'

        )
    # Prints the Twilio Message SID in the terminal
    print(outgoing_message.sid)

    # Sends a simple HTTP response back to Twilio.
    return HttpResponse("hello")





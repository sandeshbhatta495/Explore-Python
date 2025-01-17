from twilio.rest import Client
from datetime import datetime, timedelta
import time


client = Client(account_sid, auth_token)


def send_whatsapp_message():
    message = client.messages.create(
        from_='whatsapp:9779741685837',
        body='Hello! This is a test message',
        to='whatsapp:9779866534087'
    )

    print(message.sid)
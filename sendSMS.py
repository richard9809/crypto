from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "AC656a19780b4663f72e4fd44f466de53c"
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN'] = "313f6a5c22d2db48892905e305b74c9b"

client = Client(account_sid, auth_token)

def sendSMS(body, to):
    message = client.messages.create(
    to= to, 
    from_="+19896933474",
    body= body)
    return message.sid
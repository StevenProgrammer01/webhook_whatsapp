from twilio.rest import Client

account_sid = 'AC2e431a4f1421fb0b09fffc18a1315c5e'
auth_token = '1a416a8ff58a8ed9d449b5d5ef03b160'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Hello Jose Carlos, How are you?',
  to='whatsapp:+50664269796'
)

print(message.sid)
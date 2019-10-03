# Before running do this : pip install twilio

#Step 1: Get your Account_Sid and Auth token securely

from twilio.rest import Client


#  See http://twil.io/secure

#Authenticate client
account_sid = 'ENTER IN'
auth_token = 'ENTER IN'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='YOUR OWN MESSAGE!',
                              from_='YOUR TWILIO NUMBER ',
                              to='SENDING MESSAGE TO '
                          )

print(message.sid)

#to run python (Name of File).py

#STEP 2: CALLS

#Step 3: Group Messages and then group calls


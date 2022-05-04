from twilio.rest import Client

account_SID = "AC19ec6bfb1294094b0fbb2c7cc27b52fc"
token = "70997a09987c717223b451b3d88ebdec"

client = Client(account_SID, token)

message = client.messages.create(
    to="+5511962524717",
    from_="+19894558898",
    body="Hello from Python"
)

from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

from_phone_number = ''
to_phone_number = ''

# the kijiji and SPCA new puppy alerts are different because I wanted the
# information in the text message to be sent in a different order

# kijiji new puppy alert
def send_message_kijiji(title, link, description, cost):
    send_message("kijiji", title, cost, link, description)

# SPCA new puppy alert
def send_message_SPCA(title, link, description):
    send_message("SPCA", title, description, link)

# format new puppy alert
def send_message(line1, line2, line3, line4, line5=''):
    if line5 !='':
        line5 += '\n'

    body = f"!!!NEW PUPPY - {line1}!!!\n\n{line2}\n{line3}\n{line4}\n{line5}\n!!!NEW PUPPY!!!"
    twilio_send_sms(body)

# scraper started alert
def send_start_alert(site):
    body = f"{site} scraper started!"
    twilio_send_sms(body)
    
# use twilio to send sms
def twilio_send_sms(body):
    client.messages.create(body = body, from_ = from_phone_number, to = to_phone_number)
    

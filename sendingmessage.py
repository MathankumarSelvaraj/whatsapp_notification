import mongo as mg
import pandas as pd
import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
from twilio.rest import Client

file_name = mg.file_name
load_dotenv(r'key.env')

account_sid = os.getenv('YOUR_ACCOUNT_SID')
auth_token = os.getenv('YOUR_AUTH_TOKEN')

print(account_sid,auth_token)

client = Client(account_sid, auth_token)

to_send_number = os.getenv('TO_PHONE_NUMBER')

from_whatsapp_no = 'whatsapp:+14155238886'
to_whatsapp_no = "whatsapp:" + "+"+to_send_number
msg = mg.df.to_string(index=False, justify='right', line_width=50, show_dimensions=True)

media_file_path = f'D:\Mathan\Python workspace\sending_whatsapp message\{file_name}'
print(file_name)
with open(media_file_path, 'rb') as f:
    response = requests.put(f'https://temp.sh/{file_name}', data=f)
    if response.status_code == 200:
        media_url = response.text.strip()
    else:
        raise Exception("Failed to upload file to temp.sh")

print(media_url)
#with open(file_name, 'rb') as file:
# client.messages.create(body=msg,
#                        #media_url= media_url,
#                       from_=from_whatsapp_no,
#                       to=to_whatsapp_no
#                       )

print(f"Bar chart saved as {file_name} and sent via WhatsApp.")




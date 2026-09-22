import requests

from django.conf import settings


BREVO_URL="https://api.brevo.com/v3/smtp/email"

def send_email(to_email,to_name,subject,message):

    headers={
        "accept":"application/json",
        "api-key":settings.BREVO_API_KEY,
        "content-type":"application/json",
    }


    data={
        "sender":{
            "name":"KD Interiors",
            "email":"kprabu1512@gmail.com"
        },

        "to":[
            {
            "email":to_email,
            "name":to_name
            }
        ],

        "subject":subject,
        "textContent":message,
    }

    response=requests.post(
        BREVO_URL,
        headers=headers,
        json=data
    )


    if response.status_code==201:
        print("Email sent successfully")

    else:
        print("Email sending failed!")
        print("Status:",response.status_code)
        print("Response",response.text)

    return response
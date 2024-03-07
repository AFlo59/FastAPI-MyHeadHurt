import os
import mailjet_rest
from mailjet_rest import Client
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.exceptions import ImproperlyConfigured

from accounts.models import CustomUser

def send_confirmation_email(user):
    # Generate activation link
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_link = f"{os.getenv('FRONTEND_URL')}/accounts/validate_email/{uidb64}/{token}/?is_active=True"

    # Construct the email content
    email_content = render_to_string('email_templates/activation_email.html', {
        'user': user,
        'activation_link': activation_link
    })

    # Send the email using Mailjet API
    api_key = os.getenv('MAILJET_API_KEY')
    api_secret = os.getenv('MAILJET_SECRET_KEY')

    if not api_key or not api_secret:
        raise ImproperlyConfigured('MAILJET_API_KEY and/or MAILJET_SECRET_KEY are not set in environment')

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "etudessup59230@gmail.com",
                    "Name": "Admin"
                },
                "To": [
                    {
                        "Email": user.email,
                        "Name": user.username
                    }
                ],
                "Subject": "Email validation",
                "HTMLPart": email_content,
            }
        ]
    }

    try:
        response = mailjet.send.create(data=data)
        response.raise_for_status()
    except mailjet_rest.errors.MailjetError as e:
        raise Exception(f'Failed to send activation email: {str(e)}')
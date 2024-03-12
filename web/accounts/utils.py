import os
import mailjet_rest
from mailjet_rest import Client
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.http import HttpRequest

from accounts.models import CustomUser

def send_confirmation_email(request, user):
    # Generate activation link
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_link = request.build_absolute_uri(reverse('accounts:activate', kwargs={'uidb64': uidb64, 'token': token}))

    # Construct the email content
    email_content = f"Hello {user.username},\n\nPlease click on the following link to activate your account:\n{activation_link}"

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

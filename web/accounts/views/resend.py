from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator

from accounts.models import CustomUser
from accounts.views.register import RegisterView

class ResendActivationEmailView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            # Send activation email
            RegisterView().send_confirmation_email(user)
            return HttpResponse("Activation email has been resent successfully.")
        else:
            return HttpResponse("Invalid activation token.")

    def post(self, request, *args, **kwargs):
        # Handle POST requests here
        # Example code to handle POST request and resend activation email
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            # Send activation email
            RegisterView().send_confirmation_email(user)
            return HttpResponse("Activation email has been resent successfully.")
        else:
            return HttpResponse("Invalid activation token.")
from django.views.generic import View
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator

from accounts.models import CustomUser
from accounts.utils import send_confirmation_email

class ResendActivationEmailView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            send_confirmation_email(user)
            messages.success(request, 'Activation email has been resent successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid activation token.')
            return redirect('login')

    def post(self, request, *args, **kwargs):
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        user = get_object_or_404(CustomUser, pk=uidb64)

        if default_token_generator.check_token(user, token):
            # Send activation email
            send_confirmation_email(user)
            messages.success(request, 'Activation email has been resent successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid activation token.')
            return redirect('login')


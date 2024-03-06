from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import View
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from accounts.models import CustomUser

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import View
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from accounts.models import CustomUser

class ValidateEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            messages.error(request, 'Invalid activation link.')
            return redirect('accounts:register')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, 'Thank you for confirming your email address.')
            return redirect('accounts:username', username=user.username)
        else:
            messages.error(request, 'Invalid activation link.')
            return redirect('accounts:register')
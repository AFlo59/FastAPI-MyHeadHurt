from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import CustomUser
from mailjet_rest import Client

api_key = '-------------------------'
api_secret = '-------------------------'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "jeremy.vangansberg@gmail.com",
        "Name": "Jérémy"
      },
      "To": [
        {
          "Email": "jeremy.vangansberg@gmail.com",
          "Name": "Jérémy"
        }
      ],
      "Subject": "Email validation",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
class UserCreationFromCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class SignUpView(CreateView):
    form_class = UserCreationFromCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SignupView(CreateView):
    form_class = UserCreationFromCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False  # Do not activate the account immediately
        user.save()
        self.send_confirmation_email(user)
        return response

    def send_confirmation_email(self, user):
        mailjet.send.create(data=data)

    def get_success_url(self):
        # Redirect to a page informing the user to check their email
        return reverse_lazy('home')  # You should define 'home' to redirect to a view 
                                     # that allows changing the user's 'is_active' status.


@login_required
def username_page(request, username):
    return render(request, 'accounts/username.html', {'username': username})

@login_required
def profil_page(request):
    return render(request, "accounts/profil_page.html")

def custom_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
from django.contrib.auth.models import User

def create_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    return user
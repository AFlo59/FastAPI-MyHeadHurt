from django.contrib.auth.backends import ModelBackend
from django.core.mail.backends.base import BaseEmailBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
        
class ConsoleEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for message in email_messages:
            print("To:", message.to)
            print("Subject:", message.subject)
            print("Body:", message.body)
            print("----")
        return len(email_messages)
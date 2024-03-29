#accounts.forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate
from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'])
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    current_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'date_of_birth', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        current_password = cleaned_data.get('current_password')

        if password and current_password:
            user = authenticate(username=self.instance.username, password=current_password)
            if not user or not user.check_password(current_password):
                self.add_error('current_password', 'Incorrect current password')
            else:
                self.instance.set_password(password)

        return cleaned_data

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if CustomUser.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email address is already in use.')
    #     return email

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     current_password = self.cleaned_data.get('current_password')
    #     if password and not current_password:
    #         raise forms.ValidationError('Please enter your current password to change your password.')
    #     elif password and current_password:
    #         user = self.instance
    #         if not user.check_password(current_password):
    #             raise forms.ValidationError('Your current password is incorrect.')
    #     return password

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.phone_number = self.cleaned_data['phone_number']
    #     user.date_of_birth = self.cleaned_data['date_of_birth']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     if self.cleaned_data['password']:
    #         user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=_("Enter your new password."),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
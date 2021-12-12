from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django import forms


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'placeholder': 'Username'}),
        label=''
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'placeholder': 'Password'}),
    )


class UserRegistrationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'placeholder': 'Username'}),
        label=''
    )
    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder': 'Password confirmation'}),
        strip=False,
    )
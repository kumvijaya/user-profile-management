"""Custom forms in users app.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class LoginForm(AuthenticationForm):
    """Custom login form with required fields along with rememberme field

    Args:
        AuthenticationForm (obj): Base auth form
    """
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        """Meta class defines required user model with fields
        """
        model = User
        fields = ['username', 'password', 'remember_me']


class RegisterForm(UserCreationForm):
    """Custom registration form with all user model fields for creating new user

    Args:
        UserCreationForm (obj): Base registration form
    """
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        """Meta class defines required user model with fields
        """
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    """Custom user form with all user model fields for updating the existing user

    Args:
        ModelForm (obj): Base model form
    """
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """Meta class defines required user model with fields
        """
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    """Custom User form with all user model fields for updating the user with user profile
    Extended with custom fields.

    Args:
        ModelForm (obj): Base model form
    """
    address_line1 = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_line2 = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=30,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    zip_code = forms.CharField(max_length=6,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_number = forms.CharField(max_length=15,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """Meta class defines required user model with fields
        """
        model = Profile
        fields = ['address_line1', 'address_line2',
                  'city', 'zip_code', 'phone_number']

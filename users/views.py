"""Custom views in users app
"""
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm

def home(request):
    """Gets the home view

    Args:
        request (obj): request

    Returns:
        obj: view
    """
    return render(request, 'users/home.html')

@login_required
def profile(request):
    """Gets profile page view

    Args:
        request (obj): request

    Returns:
        obj: view
    """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html'
                  , {'user_form': user_form, 'profile_form': profile_form})

class CustomLoginView(LoginView):
    """Gets login page view.
    Class based view that extends from the built in login view with custom style.
    Also adds remember me functionality

    Args:
        LoginView (obj): Base view for login
    """

    def form_valid(self, form):
        """Override form validation method to add remember view function

        Args:
            form (obj): base form

        Returns:
            boolean: whether form valid
        """
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds.
            # So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time
        # i.e."SESSION_COOKIE_AGE" defined in settings.py
        return super().form_valid(form)


class RegisterView(View):
    """Gets registration page view.
    Class based view that extends from the built in view

    Args:
        RegisterView (obj): Base view for sign up
    """
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request):
        """Get Request handler. Renders the request with template.

        Args:
            request (obj): request

        Returns:
            obj: view
        """
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Post request handler. Renders the page with template after post/save.

        Args:
            request (obj): request

        Returns:
            obj: view
        """
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        """Dispatch request handler. Renders the page with template after redirect.

        Args:
            request (obj): request

        Returns:
            obj: view
        """
        # This will redirect to the home page
        # if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # Else process dispatch as it otherwise normally would
        return super().dispatch(request, *args, **kwargs)

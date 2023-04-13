from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django_admin_geomap import geomap_context
from .models import Location
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm,  UpdateUserForm, UpdateProfileForm

"""Gets home page view
"""
def home(request):
    return render(request, 'users/home.html')

"""Gets locations map page view
"""
def map(request):
    return render(request, 'map.html', geomap_context(Location.objects.all(), auto_zoom="10"))

"""Gets profile page view
"""
@login_required
def profile(request):
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

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

"""Gets login page view.
Class based view that extends from the built in login view to add a remember me functionality
"""
class CustomLoginView(LoginView):
    form_class = LoginForm

    """Override form validation method to add remember view function
    """
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

"""Gets login page view.
Class based view that extends from the built in view
"""
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    """Get request handler. Renders the request with template.
    """
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    """Post request handler. Renders the page with template after post/save.
    """
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
    
    """Dispatch request handler. Renders the page with template after redirect.
    """
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
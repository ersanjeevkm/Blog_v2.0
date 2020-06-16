from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, current_user
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}, Login to continue')
            return redirect('login')
        else:
            context = {'form': form}
    else:
        form = RegisterForm()
        context = {'form': form}
    return render(request, 'users/register.html', context)

class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_message = 'Logged in successfully'

class UserLogout(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'

@login_required
def account(request):
    if request.method == 'POST':
        current_user(request)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            messages.success(request, "Account updated successfully!")
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/account.html', context)

class Password_reset(UserPassesTestMixin, PasswordResetView):
    template_name = 'users/password_reset.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

class Password_reset_done(UserPassesTestMixin, PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

class Password_reset_confirm(UserPassesTestMixin, PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

class Password_reset_complete(UserPassesTestMixin, PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True


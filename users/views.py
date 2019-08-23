"""Users views."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.urls import reverse
from django.shortcuts import render, redirect


def login_view(request):
    """Logoin a user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('reservations:menu_list')
        else:
            return render(request, 'users/login.html', {
                'error': 'invalid username and password'
            })

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

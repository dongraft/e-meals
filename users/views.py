"""Users views."""

from django.contrib.auth import (
    authenticate,
    login
)
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/login.html', {
                'error': 'invalid username and password'
            })

    return render(request, 'users/login.html')

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ipware.ip import get_real_ip
from .forms import LogInForm
import iptools


def log_in(request):
    error = False
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LogInForm()
    if request.user.is_authenticated():
        return redirect(register)
    return render(request, 'login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse(log_in))


def index(request):
    if request.user.is_authenticated():
        return redirect(register)
    return render(request, 'index.html')


@login_required
def register(request):
    return render(request, 'register.html', {})


def queue(request):
    ip = get_real_ip(request)
    ip_int = None
    if ip is not None:
        ip_int = [int(i) for i in ip.split('.')]
    if (ip_int is not None and ip_int[-1] >= 131 and ip_int[-1] <= 195 and ip_int[0] == 164 and ip_int[1] == 15 and \
        ip_int[2] == 81) or request.user.is_authenticated():
        # we have a real, public ip address for user
        auth = True
    else:
        auth = False
    return render(request, 'queue.html', {'auth': auth})


def sign_in(request):
    return render(request, 'index.html')


@login_required
def assistant(request):
    return render(request, 'assistant.html', {})

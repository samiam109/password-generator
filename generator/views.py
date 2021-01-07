from django.shortcuts import render
import string
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 12))

    choices = string.ascii_lowercase
    if request.GET.get('uppercase'):
        choices += string.ascii_uppercase
    if request.GET.get('special_characters'):
        choices += string.punctuation
    if request.GET.get('numbers'):
        choices += string.digits

    password_is = ''.join(random.choice(choices) for _ in range(length))

    return render(request, 'generator/password.html', {'password': password_is})


def about(request):
    return render(request, 'generator/about.html')

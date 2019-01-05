from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import KamengitesOrg


def signup_add(request):
    if request.method == 'POST':
        # print("Entered if")
        u = User()
        k = KamengitesOrg()
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')
        u.username = request.POST.get('username')
        u.email = request.POST.get('email')
        k.room = request.POST.get('room')
        k.roll = request.POST.get('roll')
        p = request.POST.get('password')

        if request.POST.get('password2') == p:
            u.set_password(p)
            u.save()
            k.user = u
            k.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/login/')
        else:
            return render(request, 'accounts/not_match.html')


def signup(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if str(ip[0:4]) == "10.9":
        return render(request, "accounts/signup.html")
    else:
        return render(request, "accounts/not_match.html")
    # return render(request, "accounts/signup.html")



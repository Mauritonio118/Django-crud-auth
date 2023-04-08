from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, 'home.html')

def singup(request):

    if request.method =='GET':
        return render(request, 'singup.html', {
            "form": UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Register User
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse("<h1>User created</h1>")
            except:
                return HttpResponse("<h1>Username already exist</h1>")
        return HttpResponse("<h1>Password Fail</h1>")

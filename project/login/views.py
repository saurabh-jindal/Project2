from django.shortcuts import render
from .forms import LoginForm, SignUpForm
from .models import Signup
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    form = LoginForm()
    
    context = {
        "form":form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            if (Signup.objects.filter(email = email).exists()):
                return HttpResponseRedirect('user')
        # else:
        #     form = LoginForm()

    return render(request, 'login.html',context)

def signup(request):
    form = SignUpForm()
    context = {
        "form":form,
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            signup = Signup(
                name=form.cleaned_data["name"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
            )
            signup.save()
            return HttpResponseRedirect('/')
        
        else:
            form = SignUpForm()

    return render(request, 'signup.html',context)


def user(request):
    return render(request, 'user.html')
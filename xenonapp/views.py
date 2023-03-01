from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


# @login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')

            if pass1!=pass2:
                return HttpResponse("Your password and confrom password are not Same!!")
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Your username is already exist please!!")
            else:

                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('home')
        



    return render (request,'register.html')

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request,username=username,password=pass1)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse ("Username or Password is incorrect!!!")

        return render (request,'login.html')

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')
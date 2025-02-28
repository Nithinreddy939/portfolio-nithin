from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.
# Create your views here.

# @login_required(login_url='signin')
def index(request):
    return render(request,'index.html')

@login_required(login_url='signin')
def about(request):
    return render(request,'about.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('signin')
    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']
        if password == password2 and email not in User.objects.values_list('email',flat=True):
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
            user.save()
            return redirect('signin')
        return render(request,'signup.html')
    return render(request,'signup.html')


def signout(request):
    auth.logout(request)
    return redirect('index')
    
def display_details(request):
    data=User.objects.all()
    return render(request,'display_details.html',{'data':data})

def get_persondetails(request,username):
    data1=User.objects.get(username=username)
    return render(request,'get_persondetails.html',{'data1':data1})


@login_required(login_url='signin')
def certificate(request):
        
    return render(request,'certification.html')


@login_required(login_url='signin')
def projects(request):
    return render(request,'project.html')

@login_required(login_url='signin')
def qualification(request):
    return render(request,'qualification.html')


# membership users
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('display_details')
        else:
            return redirect('signin')
    return render(request,'signin.html')

 
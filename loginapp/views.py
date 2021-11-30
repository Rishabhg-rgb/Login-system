from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import time
from threading import Timer
# Create your views here.




def home(request):
    return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        if password1==password2 and len(username)>=1 and len(email)>=1 and len(address)>=1:
            myuser = User.objects.create_user(username,email,password1)
            myuser.first_name = address
            myuser.save()
            return redirect('/')
        else:
            return HttpResponse('Error 404 BAD REQUESt')
    else:
        return render(request,'signup.html')



def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            
            login(request,user)
            
            return redirect('/user')
        else:
            return HttpResponse('user not registered')

    return HttpResponse('error')

def handlelogout(request):
        logout(request)
        return redirect('/')

def user(request):
    
    return render(request,'index.html')

def editdetails(request,id):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        myuser = User.objects.filter(id =id).update(username=username,email=email,first_name=address)
        
        
        print(myuser)
        
        return redirect('/user')
    else:
        return redirect('/user')


def delete(request,id):
    user = User.objects.filter(id=id)
    user.delete()
    return redirect('/')
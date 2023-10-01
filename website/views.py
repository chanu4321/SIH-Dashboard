from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import status

# Create your views here.
def home(request):
    stat=status.objects.all()
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # aunthenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Sucessfully")
            return redirect('home')
        else :
            messages.success(request, "Error logging In")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': stat})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')

def bulbissue(request,Bulb_Issue):
    if request.user.is_authenticated :
        problem1 = status.objects.filter(Bulb_Issue=Bulb_Issue).first()
        return render(request, 'record.html', {'problem': problem1})
    else:
        messages.success(request, "Login to view")
        return redirect('home')

def currleak(request,Curr_Leak):
    if request.user.is_authenticated :
        problem2 = status.objects.filter(Curr_Leak=Curr_Leak).first()
        return render(request, 'record.html', {'problem': problem2})
    else:
        messages.success(request, "Login to view")
        return redirect('home')
    
def brokwire(request,Brok_Wire):
    if request.user.is_authenticated :
        problem3 = status.objects.filter(Brok_Wire=Brok_Wire).first()
        return render(request, 'record.html', {'problem': problem3})
    else:
        messages.success(request, "Login to view")
        return redirect('home')
    
def nosignal(request,No_Sgnl):
    if request.user.is_authenticated :
        problem4 = status.objects.filter(No_Sgnl=No_Sgnl).first()
        return render(request, 'record.html', {'problem': problem4})
    else:
        messages.success(request, "Login to view")
        return redirect('home')
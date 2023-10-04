from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import models

# Create your views here.
def home(request):
    
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
        context={
            'common_issues': models.CommonIssue.objects.all(),
            'current_leakage' : models.CurrentLeakeageIssue.objects.all(),
            'broken_wire' : models.BrokenWireIssue.objects.all(),
            'no_signal' : models.NoSignalIssue.objects.all(),
        }
        return render(request,'home.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


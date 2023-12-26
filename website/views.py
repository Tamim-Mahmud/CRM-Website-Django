from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

# for lgin log out message
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You Have Loged In Successfully .....")
            return redirect('home')
        else:
            messages.error(request,"Error Occured . Please Try again .....")
            return redirect('home')
    else:
        return render(request, 'home.html',{})
    
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    return redirect('home')
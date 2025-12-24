from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import Register_user
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=Register_user.objects.filter(email=email)
        if not user.exists():
            messages.warning(request,"User doesn't exist please register first")
            return redirect('register_view')
        user=authenticate(username=user[0].username,password=password)
        if user:
            login(request,user)
            return redirect('index')

    return render(request,'login.html')
def register_view(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=Register_user.objects.filter(email=email)

        if user.exists():
            messages.warning(request,"Account is already exist with Email")
            return redirect('register_view')
        user=Register_user.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.success(request,'Register succesfully')
        return redirect('register_view')
    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
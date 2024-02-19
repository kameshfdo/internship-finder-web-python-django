from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User
from .form import RegisterUserForm
from  resume.models import Resume
from company.models import Company

#register applicant only
def register_applicant(request):
    if request.method =='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.username = user.email
            user.save()
            Resume.objects.create(user=user)
            messages.info(request,'Your account has been created.plaese login')
            return redirect('login')
        else:
            messages.warning(request,'Somthing went worng')
            return redirect('register_applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register_applicant.html',context)
    
#register recuriter only
def register_recruiter(request):
    if request.method =='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter=True
            var.username=var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request,'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request,'Somthing went worng')
            return redirect('register_recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register_recruiter.html',context)

#login a user
def login_user(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,"something went wrong.")
            return redirect('login')
    else:
        return render(request,'users/login.html')
    
#logout user
def logout_user(request):
    logout(request)
    messages.info(request,"your session has been ended.")
    return redirect('login')
 
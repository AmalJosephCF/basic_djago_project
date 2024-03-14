from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(usernaem=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid entry')
            return redirect(request,'login.html')

    return render(request,'login.html')
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['f_name']
        secondname = request.POST['s_name']
        mail = request.POST['email']
        passw = request.POST['pass']
        passw1 = request.POST['pass1']
        if passw==passw1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"EMAIL  TAKEN")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=passw,first_name=firstname,last_name=secondname,email=mail,)

                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password doest match")
            print("invalid password")
            return redirect('register')

    return render(request,'register.html')

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info("Invalid Username and Password")
            return redirect('login')

    return render(request, "login.html")

def registerin(request):
    if request.method== 'POST':
        username=request.POST['Username']
        firstname = request.POST['FirstName']
        lastname = request.POST['Lastname']
        email = request.POST['Emailid']
        password = request.POST['Password']
        cpassword = request.POST['ConfirmPassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Mail Id already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email,)
                user.save();
                print("User Created Successfully")
                return redirect('login')

        else:
            print("Incorrect Password")
            return redirect('register')

        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

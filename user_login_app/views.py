from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password Invalids!')
            return redirect('login')
    else:
        return render(request, 'login.html')  

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

            
        # print(username)
        # if username == None or email == None or password == None:
        #     messages.info("Somethin went wrong, try again!")
        #     return redirect('register')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used!")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used!")
                return redirect('register')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save();
                    return redirect('login')
                except:
                    messages.info(request, "Somethin went wrong, try again!")
                    return redirect('register')

        else:
            messages.info(request, "Passwords are not the same!")
            return redirect('register')
    else:
        return render(request, 'register.html')  


def logout(request):
    auth.logout(request)
    return redirect('/')
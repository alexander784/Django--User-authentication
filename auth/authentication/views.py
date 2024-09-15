from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'authentication/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect ('/login/')
        
        login(request, user)
        return redirect('/home')
    
    return render(request, 'authentication/login.html')
    
        # else:
            # login(request, user)
            # return redirect('/home')
        

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # CHeck if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an infor message if the username is taken
            messages.info(request, 'Username already taken!')
            return redirect('/register')
        # create new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user
        user.set_password(password)
        user.save()


        # Display info indiccatinf successs creatipon of new user
        messages.info(request,"Account successfully created")
        return redirect('/register')
    
    return render(request,'authentication/register.html')
    
        

        



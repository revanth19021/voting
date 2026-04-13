from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash

from elections.models import Election, Candidate

from .models import Profile


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        role=request.POST.get('role')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        user=User.objects.create_user(
            username=username,
            password=password,
            
        )
        Profile.objects.create(user=user,role=role)
        return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            profile, created = Profile.objects.get_or_create(user=user)
            if user.profile.role == 'admin':
                return redirect('admin_dashboard') 
            else:
                return redirect('dashboard') 

        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request,'login.html')
    
    
    
def logout_view(request):
    logout(request)
    return redirect('login')
    
@login_required
def dashboard(request):
    profile=request.user.profile
    return render(request,'dashboard.html',{'profile':profile})


@login_required
def update_profile(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        address = request.POST.get('address')

        user = request.user
        profile = user.profile

        if password:
            user.password = make_password(password)
            user.save()

            update_session_auth_hash(request, user)

        profile.address = address
        profile.save()

        return redirect('dashboard')

    return render(request, 'update_profile.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')




@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return redirect('dashboard')

    elections = Election.objects.all()

    return render(request, 'admin_dashboard.html', {
        'elections': elections
    })
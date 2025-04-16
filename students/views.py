from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

from formations.models import FormationRegister,Formation



# inscription sur le site

def login_user(request):
    
    if request.method == 'POST':
        message=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('formation:formation')
        else:
            message = "information invalide"
    context = {"message":message}
    
    return render(request,'students/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('formation:accueil')


def register_user(request):
    """ Fonction d'inscription sur le page """
    message=[]
    if request.method =='POST':
        username = request.POST.get('username')
        address = request.POST.get('address')
        password = request.POST.get('password') # premier mot de passe 
        password1 = request.POST.get('password1') # confirmation de mot de passe
        email = request.POST.get('email')
        numero = str(request.POST.get('numero'))
        if password == password1:
            user = User()
            student = Student()
            user.username = username
            user.password =make_password(password)
            user.email = email
            
            student.user = user
            student.phone_number = numero
            student.address = address
            user.save()
            student.save()
            return redirect('student:login')

        context = {'message':message}
        return render(request,'student/register.html',context)

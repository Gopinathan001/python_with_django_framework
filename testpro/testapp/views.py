from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from testapp.models import Details




# Create your views here.
def home(request):
    return render(request,"home.html")



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.warning(request,"Password incorrect")
            return redirect('register')

        try:
            if User.objects.get(username=username):
                messages.info(request,"UserName Is Taken")
                return redirect('register')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('register')
        except:
            pass
        # mi=auth_user(phone=phone)
        # mi.save()
        myuser=User.objects.create_user(username,email,password1)
        myuser.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('login')
    return render(request,"register.html")

def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request,"Login successfully")
            return redirect('profile')
        else:
            messages.error(request,"Incorrect Password")
            return redirect('login')
    return render(request,"login.html")

def pro(request):
    return render(request,"profile.html")

def logout(request):
    try:
        del request.session['user']
    except:
        messages.info(request,"Logout successfully")
        return redirect('home')
    return redirect('home')


def dig(request):
    if request.method == 'POST':
        bankname = request.POST['bankname']
        Accountnumber = request.POST['Accountnumber']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        my = Details(bankname=bankname,Accountnumber=Accountnumber,password=password,eemail=email,econtact=phone)
        my.save()
        
        messages.info(request,"Data saved")
        return redirect('dis')
    else:
        return render(request,'digitalstorage.html')
    

def edit(request, id):  
    Edit = Details.objects.get(id=id)  
    print(Edit)
    return render(request,'update.html', {'reEdite':Edit})
   
    

def update(request, id):  
    BankUpdate = Details.objects.get(id=id) 
    return render(request,'update.html', {'update':BankUpdate})




def destroy(request, id):
    BankDel = Details.objects.get(id=id)  
    BankDel.delete()  
    return redirect("dis")



def dis(request):
    detail = Details.objects.all()
    return render(request,"display1.html",{'Bank':detail})


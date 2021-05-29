from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def studentregistration(request):
   if request.method == 'POST':
      username=request.POST['username']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      user_phone = request.POST['user_phone']
      Parent_Phone = request.POST['Parent_Phone']
      email=request.POST['email']
      Address_line=request.POST['Address_line']
      City=request.POST['City']
      State = request.POST['State']
      Pincode=request.POST['Pincode']
      Branch=request.POST['Branch']
      password1= request.POST['password1']
      password2 = request.POST['password2']

      if password1 == password2:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username exists')
            return redirect('studentregistration')
         elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('studentregistration')
         else:
            user = User(username=username,first_name=first_name,last_name=last_name,user_phone=user_phone,Parent_Phone=Parent_Phone,email=email,Address_line=Address_line,City=City,State=State,Pincode=Pincode,Branch=Branch,password=password1)
            user.save()
            print('user created')
            return redirect('studentlogin')
      else:
         messages.info(request,"password not matching")
         return redirect('studentregistration')
      return redirect('/')

   else:
      return render(request,'studentregistration.html')


def studentlogin(request):
   if request.method=='POST':
      username = str(request.POST['username'])
      password = str(request.POST['password'])
      print(f'Username {username}, Password: {password} ')
   
      user = authenticate(request, username=username , password=password)
      # user = student.objects.get_user(Student_USN)
      print(f'User {user}')
      if user is not None:
         login(request, user)
         return redirect("/")
      else:
         messages.info(request,'invalid creditials')
         return redirect('studentlogin')

   else:
      return render(request,'studentlogin.html')


def logout(request):
   logout(request)
   return redirect("/")



  
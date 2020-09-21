from django.shortcuts import render
from .form import UserRegister
# Create your views here.
def dashboard(request):
    if(request.method=='POST'):
        fm=UserRegister()
        if fm.is_valid():
            fm.save()
    else:
        fm=UserRegister()
        return render(request,'dashboard/addUser.html',{'form':fm})


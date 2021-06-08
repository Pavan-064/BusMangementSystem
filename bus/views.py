from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'index.html')

def announcements(request):
   return render(request,'announcements.html')

def about(request):
   return render(request,'about.html')
   
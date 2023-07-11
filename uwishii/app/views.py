from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def menu(request):
    return render(request,'app/menu.html')

def about(request):
    return render(request,'app/about.html')

def jobs(request):
    return render(request,'app/jobs.html')

def contact(request):
    return render(request,'app/contact.html')

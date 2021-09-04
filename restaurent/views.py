from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'about.html')    

def blogdetails(request):
    return render(request, 'blogdetails.html') 

def blogstandard(request):
    return render(request, 'blogstandard.html') 


def contact(request):
    return render(request, 'contact.html') 

def faq(request):
    return render(request, 'faq.html') 

def gallery(request):
    return render(request, 'gallery.html') 

def index(request):
    return render(request,'index.html')  

def index2(request):
    return render(request, 'index-2.html')

def manu(request):
    return render(request, 'manu.html') 

def restaurantdetails(request):
    return render(request, 'restaurantdetails.html') 

def restaurant(request):
    return render(request, 'restaurant.html')                             

def team(request):
    return render(request, 'team.html')     



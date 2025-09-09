from django.shortcuts import render

def index(request):
    blogs=[
        {'tittle':'My first blog','content':'This is my first blog content','author':'John'},
        {'tittle':'My second blog','content':'This is my second blog content','author':'Doe'},
        {'tittle':'My third blog','content':'This is my third blog content','author' :'Smith'}  
    ]
    context={'blogs':blogs }
    return render(request, "index.html", context) 

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request,"contact.html")


# Create your views here.


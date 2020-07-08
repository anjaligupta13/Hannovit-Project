from django.shortcuts import render
from Hannovit.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

#def index(request):
 #   return HttpResponse("Hello, Django!")

@csrf_exempt
def webpage(request):
    if(request.method=='POST'):
        d=request.POST
        Name = d.get("Name", "0")
        Pan_Number=d.get("Pan_Number","0")
        Age=d.get("Age","0")
        Gender=d.get("Gender","0")
        Email_Add = d.get("Email_Add", "0")
        User.objects.create(Name=Name,Pan_Number=Pan_Number,Age=Age,Gender=Gender,Email_Add=Email_Add)
    return render(request, 'Hannovit/webpage.html', {'Users':User.objects.all()})

@csrf_exempt
def search(request):
    Name=request.GET.get('Name')
    if(Name):
        users = list(User.objects.filter(Name__contains=Name))
        return render(request, 'Hannovit/search.html', {'Users':users[0:10],'Name':Name})
    return render(request, 'Hannovit/search.html', {'Name':""})
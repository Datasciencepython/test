from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

def index(request):

    form= RegistrationForm()
    context={
        "myregistrationform":form
    }


    return render(request,"firstapp/index.html",context)





from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import ReseidentForm
from accounts.models import Resident
# Create your views here.

def res(request):
    if request.method == "POST":
        form = ReseidentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = ReseidentForm()
    return render(request, "signup.html", {'form': form})

def show(request):
    residents = Resident.objects.all()
    return render(request, "index.html", {'residents': residents})

def edit(request, id):
    resident = Resident.objects.get(id=id)
    return render(request, "login.html", {'resident': resident})
def update (request, id):
    resident = Resident.objects.get(id=id)
    form = ReseidentForm(request.POST, instance = resident)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "login.html", {'resident' :resident})
def delete (request, id):
    resident = Resident.objects.get(id=id)
    resident.delete()
    return redirect("/show")


# def index(request):
#     return render(request, 'accounts/index.html')
#
# def login(request):
#     return render(request, 'accounts/login.html')
#
# def signup(request):
#     return render(request, 'accounts/signup.html')
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request,"index.html")

def sent_contact(request):
    name=request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message=request.POST.get("message")
    return redirect("/")
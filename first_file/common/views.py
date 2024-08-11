from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from common.models import Gallery, Contact, Video
from common.models import Cars


def home(request):
    gallery = Gallery.objects.all()
    cars = Cars.objects.all()
    video = Video.objects.all()

    context = {
        "gallery": gallery,
        "cars": cars,
        "video": video,
}
    # print(request.method) <---hatolarni tekshirish
    
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            Contact.objects.create(name = name, email = email, subject = subject, message = message)
            messages.add_message(request, messages.SUCCESS, "Your Massage has been sent successfully!")
            return HttpResponseRedirect(reverse("common:home"))
        
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Error occurred! Please try again! ')
            return HttpResponseRedirect(reverse("common:home"))
        
        # print(request.POST.get("name"))
        # print(request.POST.get("subject")) <--- hatolarni tekshirib olsih
        # print(request.POST.get("email"))
        # print(request.POST.get("massage"))
    return render(request, "index.html", context)

def about(request):
    return HttpResponse ("welcome about page")

def service(request):
    return HttpResponse ("welcome service page")
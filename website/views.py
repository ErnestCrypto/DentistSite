# Creating our views
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        return render(request, 'contact.html', {
            'name': name,
        })

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def appointment(request):
    return render(request, 'appointment.html', {})


def price(request):
    return render(request, 'price.html', {})


def services(request):
    return render(request, 'service.html', {})


def team(request):
    return render(request, 'team.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})

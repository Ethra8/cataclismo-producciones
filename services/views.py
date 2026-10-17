from django.shortcuts import render


def services(request):
    return render(request, "services/services.html")


def web_presence(request):
    return render(request, "services/web_presence.html")


def gestion_eventos(request):
    return render(request, "services/gestion_eventos.html")

def web_example_one(request):
    return render(request, "services/web_example_one.html")
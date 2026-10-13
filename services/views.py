from django.shortcuts import render


def services(request):
    return render(request, "services/services.html")


def web_presence(request):
    return render(request, "services/web_presence.html")
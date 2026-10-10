from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            send_mail(
                subject=f"Nuevo contacto: {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )

            messages.success(request, "Tu mensaje se ha enviado correctamente.")
            return redirect("home")

        messages.error(request, "Por favor, completa todos los campos.")

    return render(request, "home/index.html")
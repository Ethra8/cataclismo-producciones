import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render


logger = logging.getLogger(__name__)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Por favor, completa todos los campos.")
            return redirect("home")

        try:
            send_mail(
                subject=f"Nuevo contacto: {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
        except Exception:
            logger.exception("Error sending contact form email")
            messages.error(
                request,
                "No se ha podido enviar el mensaje. Inténtalo de nuevo más tarde.",
            )
            return redirect("home")

        messages.success(request, "Tu mensaje se ha enviado correctamente.")
        return redirect("home")

    return render(request, "home/index.html")
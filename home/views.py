import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
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
            email_message = EmailMessage(
                subject=f"Nuevo contacto: {name}",
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            email_message.send()
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
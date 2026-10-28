import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render


from .forms import ContactForm


logger = logging.getLogger(__name__)

SERVICE_LABELS = {
    "gestion_produccion_evento": "Gestión y/o Producción de Evento",
    "promocion_difusion_artistica": "Promoción y Difusión Artística",
    "desarrolo_web": "Desarrollo Web",
    "booking": "Booking",
}


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        services = request.POST.getlist("services")

        if not name or not email:
            messages.error(request, "Nombre y email son obligatorios.")
            return redirect("home")

        if not message and not services:
            messages.error(
                request,
                "Selecciona al menos un servicio o escribe un mensaje.",
            )
            return redirect("home")

        selected_services = [
            SERVICE_LABELS[service]
            for service in services
            if service in SERVICE_LABELS
        ]

        services_text = "\n".join(
            f"- {service}"
            for service in selected_services
        ) or "- No especificado"

        body = (
            f"Nombre: {name}\n"
            f"Email: {email}\n"
            f"Servicios:\n"
            f"{services_text}\n\n"
            f"Mensaje:\n"
            f"{message or 'No especificado'}"
        )

        try:
            email_message = EmailMessage(
                subject=f"Nuevo contacto: {name}",
                body=body,
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



def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        services = form.cleaned_data["services"]
        message = form.cleaned_data["message"]

        service_labels = dict(form.fields["services"].choices)
        selected_services = [service_labels[service] for service in services]

        email_body = (
            f"Nombre: {name}\n"
            f"Email: {email}\n"
            f"Servicios: {', '.join(selected_services) or 'No especificado'}\n\n"
            f"Mensaje:\n{message}"
        )

        send_mail(
            subject=f"Nuevo contacto web — {name}",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        messages.success(
            request,
            "Mensaje enviado correctamente. Te responderemos lo antes posible.",
        )
        return redirect("contact")

    return render(request, "home/contact.html", {"form": form})
from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("", views.services, name="services"),
    path("web-presence/", views.web_presence, name="web_presence"),
    path("gestion-eventos/", views.gestion_eventos, name="gestion_eventos"),
    path("web-example-one/", views.web_example_one, name="web_example_one"),
]
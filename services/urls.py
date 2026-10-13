from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("", views.services, name="services"),
    path("web-presence/", views.web_presence, name="web_presence"),
    # path("artist-promotion/", views.artist_promotion, name="artist_promotion"),
    # path("event-management/", views.event_management, name="event_management"),
    # path(
    #     "booking-representation/",
    #     views.booking_representation,
    #     name="booking_representation",
    # ),
]
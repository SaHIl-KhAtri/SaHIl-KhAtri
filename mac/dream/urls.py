
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index , name="dreamHome"),
    path("about", views.about , name="Aboutus"),
    path("contact", views.contact , name="contactus"),
    path("productview", views.productview , name="prodview"),
    path("tracker", views.tracker , name="trackus"),
    path("search", views.search , name="searchus"),
    path("cheackout", views.cheackout , name="cheakus"),
]

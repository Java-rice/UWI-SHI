from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("menu",views.menu,name="menu"),
    path("about",views.about,name="about"),
    path("jobs",views.jobs,name="jobs"),
    path("contact",views.contact,name="contact"),

]

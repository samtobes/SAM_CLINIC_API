from django.urls import path
from .views import ALLPatients,PatientDetailpage,PatientSignup

urlpatterns = [
    path("all/", ALLPatients.as_view(), name="home"),
    path("signup/", PatientSignup.as_view(), name="patient_detail"),
    path("<uuid:id>/", PatientDetailpage.as_view(), name="patient")
]
from django.urls import path

from .views import create_resume, resumes, resume


urlpatterns = [
    path("", resumes, name="resumes"),
    path("resume/", resume, name="resume"),
    path("create/", create_resume, name="create_resume")
]

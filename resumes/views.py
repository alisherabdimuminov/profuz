from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Resume


@api_view(http_method_names=["POST"])
def create_resume(request):
    # print(request.data)
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    birth_date = request.data.get("birth_date")
    city = request.data.get("city")
    education = request.data.get("education")
    mother_lang = request.data.get("mother_lang")
    email = request.data.get("email")
    phone = request.data.get("phone")
    new = Resume.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        city=city,
        education=education,
        mother_lang=mother_lang,
        email=email,
        phone=phone
    )
    print(new)
    return Response()


@api_view(http_method_names=["GET"])
def resumes(request):
    resumes = Resume.objects.all()
    d = []
    for resume in resumes:
        d.append({
            "first_name": resume.first_name,
            "last_name": resume.last_name,
            "phone": resume.phone,
            "email": resume.email,
            "city": resume.city,
            "birth_date": resume.birth_date,
            "education": resume.education,
            "mother_lang": resume.mother_lang,
            # "image": request.build_absolute_uri(resume.image.url)
        })
    return Response(d)

@api_view(http_method_names=["GET"])
def resume(request):
    resume = Resume.objects.last()
    d = {
        "first_name": resume.first_name,
        "last_name": resume.last_name,
        "phone": resume.phone,
        "email": resume.email,
        "city": resume.city,
        "birth_date": resume.birth_date,
        "education": resume.education,
        "mother_lang": resume.mother_lang,
        # "image": request.build_absolute_uri(resume.image.url)
    }
    return Response(d)

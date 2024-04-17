from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job


@api_view(http_method_names=['GET'])
def jobs(request):
    name = request.GET.get('job') or ""
    jobs = Job.objects.filter(title__icontains=name)
    d = []
    for job in jobs:
        d.append({
            "title": job.title,
            "category": job.category,
            "description": job.description,
            "image": request.build_absolute_uri(job.image.url),
            "price": job.price,
            "location": job.location,
        })
    return Response(d)

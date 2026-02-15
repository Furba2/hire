from django.shortcuts import render
from .models import Service, Problem

# Create your views here.

def index(request):
    return render(request, 'Hire/index.html')

def services(request):

    services = Service.objects.order_by('id')
    context = {'services': services}
    return render(request, 'Hire/services.html', context)

def service(request, service_id):

    service = Service.objects.get(id=service_id)
    problems = service.problem_set.order_by('id')
    context = {'service': service, 'problems': problems}
    return render(request, 'Hire/service.html', context)
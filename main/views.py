from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home_view(request):
    return HttpResponse(
        "<h1>Bosh sahifa!</h1>"
    )

def info_view(request):
    import datetime
    now = datetime.datetime.now()
    context = {
        "now": now,
    }
    return render(request, 'info.html', context)


def talabalar_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar.html', context)


def talaba_view(request, student_id):
    talaba = Talaba.objects.get(id=student_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba-details.html', context)
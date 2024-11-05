from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

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
    search = request.GET.get('search', None)
    talabalar = Talaba.objects.all()
    if search is not None:
        talabalar = talabalar.filter(ism__icontains=search)

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


def talaba_del_view(request, student_id):
    talaba = get_object_or_404(Talaba, id=student_id)
    talaba.delete()
    return redirect('talabalar')


def recordlar_view(request):
    search = request.GET.get('search', None)
    recordlar = Record.objects.all()
    if search is not None:
        recordlar = recordlar.filter(
            Q(talaba__ism__contains=search) |
            Q(kitob__nom__contains=search) |
            Q(kutubxonachi__ism__contains=search)
        )
    context = {
        'recordlar': recordlar
    }
    return render(request, 'recordlar.html', context)







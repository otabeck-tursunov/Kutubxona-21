from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.template.context_processors import request
from django.views.generic import UpdateView

from .models import *
from .forms import *


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
    if request.method == "POST":
        form = TalabaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Talaba.objects.create(
                ism=data['ism'],
                guruh=data['guruh'],
                kurs=data['kurs'],
                kitob_soni=data['kitob_soni'],
            )
        return redirect('talabalar')
    search = request.GET.get('search', None)
    talabalar = Talaba.objects.all()
    if search is not None:
        talabalar = talabalar.filter(ism__icontains=search)

    form = TalabaForm()
    context = {
        'talabalar': talabalar,
        'form': form
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


def kitoblar_view(request):
    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('kitoblar')
    kitoblar = Kitob.objects.all()
    mualliflar = Muallif.objects.all()
    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar,
        'form': KitobForm
    }
    return render(request, 'kitoblar.html', context)



def talaba_update_view(request, student_id):
    talaba = get_object_or_404(Talaba, id=student_id)
    if request.method == "POST":
        talaba.ism = request.POST['ism']
        talaba.guruh = request.POST['guruh']
        talaba.kurs = request.POST['kurs']
        talaba.kitob_soni = request.POST['kitob_soni']
        talaba.save()
        return redirect('talabalar')
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_update.html', context)


def kitob_update_view(request, book_id):
    kitob = get_object_or_404(Kitob, id=book_id)
    if request.method == "POST":
        muallif = get_object_or_404(Muallif, id=request.POST['muallif_id'])
        kitob.nom = request.POST['nom']
        kitob.janr = request.POST['janr']
        kitob.sahifa = request.POST['sahifa']
        kitob.muallif = muallif
        kitob.save()
        return redirect('kitoblar')
    context = {
        'kitob': kitob,
        'mualliflar': Muallif.objects.all()
    }
    return render(request, 'kitob_update.html', context)




# METHODS: GET -> o'qib olish (READ, DELETE)
#          POST -> qo'shish (CREATE, UPDATE)




# if request.method == "POST":
#     kitob_id = request.POST.get('kitob_id')
#     talaba_id = request.POST.get('talaba_id')
#
#
#     Record.objects.create(
#         kitob=Kitob.objects.get(id=kitob_id),
#         talaba=Talaba.objects.get(id=talaba_id),
#     )
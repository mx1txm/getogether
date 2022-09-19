from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return render(request, 'vereinsapp/templates/landingpage.html', {})
    return render(request, 'landingpage.html', {})

def angebote(request):

    return render(request, 'angebote.html', {})

def angebotsprofil(request):

    return render(request, 'angebotsprofil.html', {})

def nutzerprofil(request):

    return render(request, 'nutzerprofil.html', {})

def vereinsmarketing(request):

    return render(request, 'vereinsmarketing.html', {})

def anzeige_new(request):

    return render(request, 'anzeige_new.html', {})
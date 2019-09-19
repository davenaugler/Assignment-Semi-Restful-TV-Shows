from django.shortcuts import render,  redirect
from datetime import datetime

from .models import Shows

# Create your views here.


def index(request):  # GET
    return redirect("/shows")


# ******************************

def AddShowView(request):  # GET
    context = {
        'shows': Shows.objects.all()
    }

    return render(request, "srt_app/AddShow.html", context)


def AddShow(request):  # POST
    # id = 0
    print(request.POST)
    release_date = ('%m-%d-%Y')

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']

    show = Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
    # print(context['shows'].values())

    # if request.method == "POST":
    #     pass
    return redirect(f"/shows/{show.id}")


def AllShows(request):  # GET
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, "srt_app/DisplayShows.html", context)


def EditShowView(request, id):  # GET
    print(f"EditShow --> id: {id}")
    context = {
        'show': Shows.objects.get(id=id)
    }

    return render(request, "srt_app/EditShow.html", context)


def EditShow(request, id):  # POST

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']


    show = Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
    

    return redirect(f"/shows/{show.id}")


def ShowView(request, id):  # GET
    context = {
        'show': Shows.objects.get(id=id)
    }
    return render(request, "srt_app/OneShow.html", context)


def DeleteShow(request, id):  # POST
    show = Shows.objects.get(id=id)
    show.delete()

    return redirect(f"/shows")

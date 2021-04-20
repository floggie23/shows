from django.shortcuts import render, HttpResponse , redirect
from showsapp2.models import *

 #route /shows   GET
def index(request):
    context = {
        "shows" : Show.objects.all()    
    }
    return render(request, "index.html",context)
#route /shows/new   GET
def new(request):
    return render(request, "new.html")

#route /shows/create    POST
def create(request):
    print(request.POST)
    show = Show.objects.create(title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        desc=request.POST['desc'])
    return redirect("/shows/"+str(show.id))

#route /shows/<str:id>  GET

def show(request,id):
    context = {
    	"show": Show.objects.get(id=id)
    }        
    return render(request, "show.html", context)

#route /shows/<str:id>/edit     GET
def edit(request,id):
    context = {
    	"show": Show.objects.get(id=id)
    }        
    return render(request, "edit.html", context)

#route /shows/<str:id>     GET
def update(request,id):
    show = Show.objects.get(id=id)
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.release_date=request.POST['release_date']
    show.desc=request.POST['desc']
    show.save()
    return redirect("/shows/"+str(show.id))

#route /shows/<str:id>/delete    GET
def destroy(request,id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")






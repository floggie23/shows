from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/new")
    else:
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
        "show2" : Show.objects.get(id=id)
    }      
    return render(request,"edit.html", context)

#route /shows/<str:id>     GET
def update(request,id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/"+ str(id)+"/edit")
    else :
        show = Show.objects.get(id=id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.desc=request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect("/shows/"+str(show.id))

#route /shows/<str:id>/delete    GET
def destroy(request,id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")






from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event, Organizer
from .forms import EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, "myapp/events.html", context)

def event_detail(request, id):
    event = Event.objects.get(id=id)
    context = {'event': event}
    return render(request,"myapp/event-detail.html", context)


@login_required
def create_event(request):
    form = EventForm(request.POST,request.FILES or None)
    if request.method=="POST":
        if form.is_valid():
            event = form.save(commit=False)
            organizer, created = Organizer.objects.get_or_create(
                user=request.user,
                defaults={'name': request.user.username},
            )
            event.organizer = organizer
            event.save()
            form.save_m2m()
            return redirect('myapp:events')
    return render(request,"myapp/create_event.html",{'form': form})

@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)
    if request.method=="POST":
        form = EventForm(request.POST, request.FILES or None, instance=event)
        if form.is_valid():
            form.save()
            return redirect('myapp:events')
    else:
        form = EventForm(instance=event)
    
    return render(request,"myapp/edit_event.html",{'form': form})

@login_required
def delete_event(request, id):
    event = Event.objects.get(id=id)
    if request.method=="POST":
        event.delete()
        return redirect('myapp:events')
    
    return render(request,"myapp/delete_event.html")

def dashboard(request):
    organizer, created = Organizer.objects.get_or_create(user=request.user,defaults={'name': request.user.username})
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, "myapp/dashboard.html", context)
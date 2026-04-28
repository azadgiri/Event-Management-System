from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Event, Registration
from .forms import RegistrationForm

def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            return redirect(reverse('registration_success', args=[event.id]))
    else:
        form = RegistrationForm()
        
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

def registration_success(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/success.html', {'event': event})

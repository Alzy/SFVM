from django.shortcuts import render
from events.models import Event
from events.forms import EventForm
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # dictionary containing dynamic page content
    event_list = Event.objects.filter(
        approved=True
    ).order_by('start_date')[:10]

    context_dict = {
        'heading': 'Upcoming Events',
        'events': event_list
    }
    return render(request, 'events/index.html', context=context_dict)


# Events details page
def event_details(request, event_slug):
    context_dict = {}
    try:
        event = Event.objects.get(slug=event_slug)
        context_dict['event'] = event
    except Event.DoesNotExist:
        context_dict['event'] = None
    return render(request, 'events/event-details.html', context_dict)


def add_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'events/event-submitted.html')
        else:
            print(form.errors)

    return render(request, 'events/add-event.html', {'form': form})

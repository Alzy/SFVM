from django.shortcuts import render
from events.models import Event
from events.forms import EventForm
from datetime import date
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def index(request):
    # dictionary containing dynamic page content
    event_list = Event.objects.filter(
        approved=True,
        end_date__gte=date.today()
    ).order_by('start_date')[:14]

    context_dict = {
        'heading': 'Upcoming Events',
        'events': event_list
    }
    return render(request, 'events/index.html', context=context_dict)


def about(request):
    return render(request, 'events/about.html', context={})


# Events details page
def event_details(request, event_slug):
    context_dict = {}
    try:
        event = Event.objects.get(slug=event_slug)
        context_dict['event'] = event
    except Event.DoesNotExist:
        context_dict['event'] = None
    return render(request, 'events/event-details.html', context_dict)


def submitted_event(request):
    return render(request, 'events/event-submitted.html')


def submit_event(request):
    form = EventForm()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'events/event-submitted.html')
        else:
            print(form.errors)

    return render(request, 'events/submit-event.html', {'form': form})

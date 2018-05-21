from django.shortcuts import render
from events.models import Event
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # dictionary containing dynamic page content
    event_list = Event.objects.order_by('created_at')[:10]
    context_dict = {
        'heading': 'Upcoming Events',
        'events': event_list
    }
    return render(request, 'events/index.html', context=context_dict)

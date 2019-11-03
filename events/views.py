from django.shortcuts import render
from events.models import Event
from events.forms import EventForm
from datetime import date
from django.views.decorators.cache import never_cache

from events.models import Event
from events.serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status


# Create your views here.
@never_cache
def index(request):
    # dictionary containing dynamic page content
    event_list = Event.objects.filter(
        approved=True,
        end_date__gte=date.today()
    ).order_by('start_date')[:14]

    context_dict = {
        'isMobileView': (request.GET.get('mobile-app-view', None)),
        'heading': 'Upcoming Events',
        'events': event_list
    }
    return render(request, 'events/index.html', context=context_dict)


def about(request):
    context_dict = {
        'isMobileView': (request.GET.get('mobile-app-view', None)),
    }
    return render(request, 'events/about.html', context=context_dict)


# Events details page
def event_details(request, event_slug):
    context_dict = {
        'isMobileView': (request.GET.get('mobile-app-view', None)),
    }
    try:
        event = Event.objects.get(slug=event_slug)
        context_dict['event'] = event
    except Event.DoesNotExist:
        context_dict['event'] = None
    return render(request, 'events/event-details.html', context=context_dict)


def submitted_event(request):
    context_dict = {
        'isMobileView': (request.GET.get('mobile-app-view', None)),
    }
    return render(request, 'events/event-submitted.html', context=context_dict)


def submit_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'events/event-submitted.html')
        else:
            print(form.errors)

    context_dict = {
        'isMobileView': (request.GET.get('mobile-app-view', None)),
        'form': form
    }
    return render(request, 'events/submit-event.html', context=context_dict)


class EventList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    List all events, or create a new event.
    """

    def get(self, request, format=None):
        events = Event.objects.all()

        past = self.request.query_params.get('past', None)
        if past is not None:
            events = events.filter(
                approved=True,
                end_date__lte=date.today()
            ).order_by('-start_date')
        else:
            print('h')
            # Return default view. (next 14 events)
            events = events.filter(
                # approved=True,
                end_date__gte=date.today()
            ).order_by('start_date')[:14]

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

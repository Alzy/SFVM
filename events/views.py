from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # dictionary containing dynamic page content
    context_dict = {
        'heading': 'Upcoming Events'
    }
    return render(request, 'events/index.html', context=context_dict)

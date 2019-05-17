from django.shortcuts import render


# Create your views here.
def map(request):
    return render(request, 'artists/index.html', context={})

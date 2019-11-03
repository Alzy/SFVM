"""sfvm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from events import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/', include('events.urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^submit-event/', views.submit_event, name='submit_event'),
    # url(r'^submitted-event/', views.submitted_event, name='submitted_event'),
    url(
        r'^add-event/',
        RedirectView.as_view(
            url='/submit-event',
            permanent=True
        ),
        name='add_event'
    ),
    url(
        r'^music-map/',
        TemplateView.as_view(template_name='music-map.html')
    ),
    url(r'^admin/', admin.site.urls),
    path('api/v1/events/', views.EventList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
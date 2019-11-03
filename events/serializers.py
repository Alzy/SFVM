from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'name',
            'created_at',
            'slug',
            'image',
            'short_description',
            'description',
            'address',
            'city',
            'start_date',
            'end_date',
            'price',
            'more_details_link'
        ]

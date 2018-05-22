from django import forms
from events.models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="Event Name"
    )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    approved = forms.CharField(widget=forms.HiddenInput(), required=False)

    location = forms.CharField(
        max_length=128,
        help_text="Address"
    )
    image = forms.ImageField(help_text="Event image", required=False)
    description = forms.Textarea()
    start_date = forms.DateTimeField(help_text="Start date & time")
    end_date = forms.DateTimeField(help_text="End date & time")
    price = forms.DecimalField(help_text="Price", decimal_places=2, initial=0)
    more_details_link = forms.URLField(help_text="Event Link")

    class Meta:
        model = Event
        exclude = (
            'created_at',
            'approved',
            'approved_at',
        )

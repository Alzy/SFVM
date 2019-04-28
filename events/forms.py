from django import forms
from django.core.files.images import get_image_dimensions
from events.models import Event


class EventForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="* Event Name"
    )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    approved = forms.CharField(widget=forms.HiddenInput(), required=False)

    address = forms.CharField(
        max_length=128,
        help_text="* Address"
    )
    city = forms.CharField(
        max_length=64,
        help_text="* City"
    )
    image = forms.ImageField(
        help_text="Event Flyer",
        required=False
    )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "This is what will show up in the events list..."
        }),
        help_text="* Short Description",
        max_length=256
    )
    description = forms.CharField(
        widget=forms.Textarea,
        help_text="* Long Description"
    )
    start_date = forms.DateTimeField(help_text="* Start Date/Time")
    end_date = forms.DateTimeField(help_text="End Date/Time")
    price = forms.DecimalField(help_text="* Price ($0.00 if free)", decimal_places=2, initial="0.00")
    more_details_link = forms.URLField(help_text="Event Link", required=False)

    class Meta:
        model = Event
        exclude = (
            'created_at',
            'approved',
            'approved_at',
        )

    # def clean_image(self):
    #     img = self.cleaned_data.get("image")
    #     if not img:
    #         pass
    #     else:
    #         w, h = get_image_dimensions(img)
    #         if w != h:
    #             raise forms.ValidationError("The image must be a square and 800x800px or smaller.")
    #         if w > 800 or h > 800:
    #             raise forms.ValidationError("The image must be a square and 800x800px or smaller.")
    #     return img

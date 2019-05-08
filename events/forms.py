from django import forms
from django.core.files.base import ContentFile
from django.core.files.images import get_image_dimensions
from django.core.files.uploadedfile import InMemoryUploadedFile
from events.models import Event

from PIL import Image
from io import BytesIO

import os
import re
import base64


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
    image_base64_text = forms.CharField(
        widget=forms.HiddenInput(),
        help_text="Image Base4",
        required=False
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
        # I've defined fields here to ensure 'image_base64_text' appears before 'image'
        # This also ensures it is cleaned first.
        fields = (
            'name',
            'image_base64_text',
            'image',
            'short_description',
            'description',
            'address',
            'city',
            'start_date',
            'end_date',
            'price',
            'more_details_link'
        )

    def clean_image(self):
        img = self.cleaned_data.get("image")
        imageData = self.cleaned_data.get("image_base64_text")
        if not img:
            return img
        if not imageData:
            return img
        

        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        imageData = dataUrlPattern.match(imageData).group(2)

        # If none or len 0, means illegal image data
        if (imageData == None or len(imageData) == 0):
            # PRINT ERROR MESSAGE HERE
            print('corrupt or illegal image data')

        # Decode the 64 bit string into 32 bit
        imageData = base64.b64decode(imageData)
        imageData = Image.open(BytesIO(imageData))
        imageBuffer = BytesIO()
        imageData.convert('RGB')
        imageData.save(fp=imageBuffer, format='JPEG')
        imageContent = ContentFile(imageBuffer.getvalue())

        return InMemoryUploadedFile(
            # file(ContentFile)
            imageContent,
            # field_name(idk)
            None,
            # name
            img.name,
            # content_type
            'image/jpeg',
            # size
            imageContent.tell,
            # charset(idk)
            None
        )


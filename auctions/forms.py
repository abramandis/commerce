# forms.py
from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

    #overriding save method to add additional operations    
    def save(self, commit=True):
        instance = super(ListingForm, self).save(commit=False)
        # Perform additional operations with the instance, if needed
        if commit:
            instance.save()
        return instance
        
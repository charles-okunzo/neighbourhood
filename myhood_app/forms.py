from django import forms
from .models import *

class NeighbourhoodCreateForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['hood_name', 'description', 'hood_loc', 'hood_image','contact_info']
        
    def __init__(self, *args, **kwargs):
        super(NeighbourhoodCreateForm, self).__init__(*args, **kwargs)
        self.fields['hood_name'].widget.attrs.update({'placeholder':'Enter the name of your hood...'})
        self.fields['description'].widget.attrs.update({'placeholder':'Describe your neighbourhood...'}),
        self.fields['hood_loc'].widget.attrs.update({'placeholder':'Enter your hoods location...'}),
        self.fields['contact_info'].widget.attrs.update({'placeholder':'Enter emergency contact info...'}),

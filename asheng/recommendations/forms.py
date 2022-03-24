from django import forms
from .models import *

class UserInputsForm(forms.ModelForm):
    #Form for the search image model"
    class Meta:
        model = UploadingUserInputs
        fields = [ 'title', 'genre']
from django import forms
from .models import *


class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply
        fields = ['applier_name', 'applier_phone', 'message']



from django import forms
from accounts.models import Resident

class ReseidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = "__all__"
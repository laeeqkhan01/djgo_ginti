from django  import forms
from .models import AdadTable

class AdadForm(forms.ModelForm):
  class Meta:
    model  = AdadTable
    fields = ('num', 'sound')

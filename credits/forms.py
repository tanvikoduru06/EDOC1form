from django import forms
from credits.models import Transaction

class NewTransaction(forms.ModelForm):
    class Meta():
        model=Transaction
        fields='__all__'



from django import forms
from .models import List_People

class ListPeopleForm(forms.ModelForm):
    class Meta:
        model = List_People
        fields = ('user', 'surname', 'name', 'birthday', 'mobile_phone')
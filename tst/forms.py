from django import forms
from tst import parse
from tst.models import Main


class AddBd(forms.ModelForm):
    class Meta:
        model = Main
        fields = ('region', 'country', 'value')


class PostForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ('region', 'country', 'value',)
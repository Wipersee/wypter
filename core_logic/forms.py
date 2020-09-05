from django import forms
from . import models


class AddExtendForm(forms.ModelForm):

    class Meta:
        model = models.Extend
        fields = ('category', 'price', 'comment')


class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = ('price',)

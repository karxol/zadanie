from django import forms
from .models import Expense
from django.db import models


class ExpenseSearchForm(forms.ModelForm):
    """from_date = models.DateField()
    to_date = models.DateField()"""
    date_modified = models.DateTimeField(blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    class Meta:
        model = Expense
        fields = ('name', 'category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


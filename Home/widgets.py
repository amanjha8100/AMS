from django.forms import DateInput
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'
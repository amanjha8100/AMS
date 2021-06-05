from django import forms
from . models import attendance,time
from . widgets import DateInput
import datetime
from django.core.exceptions import ValidationError
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ("name","roll","date","sub")

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'roll':forms.NumberInput(attrs={'class':'form-control','placeholder':'Roll Number(60--)'}),
            #'date':forms.DateInput(attrs={'class':'form-control form-label'}),
            'sub':forms.Select(attrs={'class':'form-control','placeholder':'Subject'}),
            # 'time':forms.Select(attrs={'class':'form-control','placeholder':'Day'}),
            'date':DateInput,
        }

        def clean_date(self):
            date_passed = self.cleaned_data['date']
            print(date_passed)
            if date_passed is not datetime.datetime.today():
                raise ValidationError("You can only enter attendance for today.")
            return date_passed
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label=""
        self.fields['roll'].label=""
        self.fields['date'].label=""
        self.fields['sub'].label=""
        # self.fields['time'].label=""
        # self.fields['time'].queryset = time.objects.none()
        
        # if 'sub' in self.data:
        #     try:
        #         sub_id = int(self.data.get('sub'))
        #         self.fields['time'].queryset = time.objects.filter(sub_id=sub_id).order_by('time')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
            #self.fields['time'].queryset = self.instance.country.city_set.order_by('time')
from django import forms

from meditech.models import Students
#from students.models import Students
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
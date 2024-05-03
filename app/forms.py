from django import forms
from .models import Applicant, Document


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['full_name', 'gender', 'birth_date', 'email', 'school']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']
        readonly_fields = ['type']
from django import forms

class DiagnosisForm(forms.Form):
	diagnosis = forms.CharField()
	recommendations = forms.CharField()
from django import forms

class UploadPlanilhaForm(forms.Form):
    arquivo = forms.FileField()
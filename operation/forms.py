from django import forms

class testingForm(forms.Form):
  kode = forms.CharField(max_length=5)
  nama = forms.CharField(max_length=30)
  deskripsi = forms.CharField()
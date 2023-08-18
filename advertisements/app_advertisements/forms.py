from django import forms

class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs = {"class":"form-control form-control-lg"}))
    descriptions = forms.CharField(widget=forms.Textarea(attrs = {"class":"form-control form-control-lg"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs = {"class":"form-control form-control-lg"}))
    trade = forms.BooleanField(required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control form-control-lg"}))
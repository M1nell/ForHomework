from django import forms
from .models import advertisement

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=120, widget=forms.TextInput(attrs = {"class":"form-control form-control-lg"}))
#     descriptions = forms.CharField(widget=forms.Textarea(attrs = {"class":"form-control form-control-lg"}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs = {"class":"form-control form-control-lg"}))
#     trade = forms.BooleanField(required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control form-control-lg"}))

class AdvertisementForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['descriptions'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['trade'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = advertisement
        fields = ("title","descriptions","price","trade","image")
from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError

# создаем класс формы, наследуя от джанговского класса
# class AdvertisementForm(forms.Form):
#     # указываем поля нашей формы, которые нужно заполнить (согласно базе данных)
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}))
#     description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control form-control-lg"}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}))
#     # кроме user, date_added и date_update - они заполнятся автоматом

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "auction", "image"]
        widget = {
            'title': forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            'description': forms.Textarea(attrs={"class": "form-control form-control-lg"}),
            'price':  forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
            'auction': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'image': forms.FileInput(attrs={"class": "form-control form-control-lg"})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.startswith("?"):
            raise ValidationError("Заголовок не может начинаться со специального символа!")
        return title

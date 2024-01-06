from django import forms


class TextForm(forms.Form):
    text_field = forms.CharField(label="Votre texte", max_length=100)

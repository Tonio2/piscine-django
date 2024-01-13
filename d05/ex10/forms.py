from django import forms
from .models import Movies, People, Planets


class PeopleForm(forms.Form):
    queryset = (
        People.objects.all()
        .values_list("gender", flat=True)
        .distinct()
        .exclude(gender="none")
    )

    minReleaseDate = forms.DateField(required=True)
    maxReleaseDate = forms.DateField(required=True)
    minDiameter = forms.IntegerField(required=True)
    gender = forms.ChoiceField(
        choices=[(gender, gender) for gender in queryset], required=True
    )  # Initialize with empty queryset

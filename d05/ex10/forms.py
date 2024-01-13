from django import forms
from .models import Movies, People, Planets


class PeopleForm(forms.Form):
    minReleaseDate = forms.DateField(required=True)
    maxReleaseDate = forms.DateField(required=True)
    minDiameter = forms.IntegerField(required=True)
    gender = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        queryset = (
            People.objects.all()
            .values_list("gender", flat=True)
            .distinct()
            .exclude(gender="none")
        )
        self.fields["gender"].choices = [(gender, gender) for gender in queryset]

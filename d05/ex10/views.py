from django.http import HttpResponse
from django.shortcuts import render
from .forms import PeopleForm
from .models import People, Planets, Movies


# Create your views here.
def index(request):
    try:
        html = None
        if request.method == "POST":
            form = PeopleForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                movie_ids = Movies.objects.filter(
                    release_date__gte=data["minReleaseDate"],
                    release_date__lte=data["maxReleaseDate"],
                )
                people = People.objects.filter(
                    movies__in=movie_ids,
                    homeworld__diameter__gte=data["minDiameter"],
                    gender=data["gender"],
                ).distinct()

                print(str(people.query))

                html = "Nothing corresponding to your research"
                if people:
                    html = "<table><tr><th>Name</th><th>Gender</th><th>Homeworld</th><th>Movie</th><th>Diameter</th></tr>"
                    for person in people:
                        for movie in person.movies.all():
                            html += f"<tr><td>{person.name}</td><td>{person.gender}</td><td>{person.homeworld.name}</td><td>{movie.title}</td><td>{person.homeworld.diameter}</td></tr>"
                    html += "</table>"
            else:
                print("Invalid form :")
                print(form.data)
                print(form.errors)
                submitted_gender = form.data.get("gender")
                print("Submitted gender value:", submitted_gender)

        else:
            form = PeopleForm()
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}", status=500)

    context = {"form": form, "html": html}
    return render(request, "ex10/index.html", context)

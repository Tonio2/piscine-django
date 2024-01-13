import os
import django
import json

# Configuration de l'environnement Django pour le script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d05.settings")
django.setup()

from ex10.models import Planets, People, Movies


def main():
    with open("ex10_initial_data.json", "r") as file:
        json_data = json.load(file)
        for elm in json_data:
            try:
                if elm["model"] == "ex10.planets":
                    Planets.objects.create(
                        id=elm["pk"],
                        name=elm["fields"]["name"],
                        climate=elm["fields"]["climate"],
                        diameter=elm["fields"]["diameter"],
                        orbital_period=elm["fields"]["orbital_period"],
                        population=elm["fields"]["population"],
                        rotation_period=elm["fields"]["rotation_period"],
                        surface_water=elm["fields"]["surface_water"],
                        terrain=elm["fields"]["terrain"],
                    )
                elif elm["model"] == "ex10.people":
                    planet = None
                    try:
                        planet = Planets.objects.get(id=elm["fields"]["homeworld"])
                    except Exception as e:
                        print(e)
                    person = People.objects.create(
                        id=elm["pk"],
                        name=elm["fields"]["name"],
                        birth_year=elm["fields"]["birth_year"],
                        gender=elm["fields"]["gender"],
                        eye_color=elm["fields"]["eye_color"],
                        hair_color=elm["fields"]["hair_color"],
                        height=elm["fields"]["height"],
                        mass=elm["fields"]["mass"],
                        homeworld=planet,
                    )
                    print(person)
                elif elm["model"] == "ex10.movies":
                    movie = Movies.objects.create(
                        episode_nb=elm["pk"],
                        title=elm["fields"]["title"],
                        opening_crawl=elm["fields"]["opening_crawl"],
                        director=elm["fields"]["director"],
                        producer=elm["fields"]["producer"],
                        release_date=elm["fields"]["release_date"],
                    )
                    for character in elm["fields"]["characters"]:
                        try:
                            movie.characters.add(People.objects.get(id=character))
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()

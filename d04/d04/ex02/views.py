from django.shortcuts import render
from .forms import TextForm
import datetime
import os
from django.conf import settings


def log(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text_field"]
            timestamp = datetime.datetime.now()
            # Écrivez dans le fichier de log et mettez à jour l'historique
            update_history_and_log(text, timestamp)
    else:
        form = TextForm()

    context = {
        "form": form,
        "history": read_history(),  # Fonction pour lire l'historique
    }
    return render(request, "ex02/log.html", context)


def update_history_and_log(text, timestamp):
    with open(settings.LOG_FILE_PATH, "a") as file:
        file.write(f"{timestamp}: {text}\n")


def read_history():
    if os.path.exists(settings.LOG_FILE_PATH):
        with open(settings.LOG_FILE_PATH, "r") as file:
            return file.readlines()
    return []

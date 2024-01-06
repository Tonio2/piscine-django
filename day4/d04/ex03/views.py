from django.shortcuts import render


def shade(request):
    opacity_levels = [i / 50 for i in range(51)]  # Adjust the range as needed
    context = {
        "range": range(51),
        "colors": [
            {
                "black": f'style="background-color: rgba(0, 0, 0, {opacity})"',
                "red": f"style='background-color: rgba(255, 0, 0, {opacity})'",
                "blue": f"style='background-color: rgba(0, 0, 255, {opacity})'",
                "green": f"style='background-color: rgba(0, 128, 0, {opacity})'",
            }
            for opacity in opacity_levels
        ],
    }
    return render(request, "ex03/index.html", context)

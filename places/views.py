from django.shortcuts import render, redirect
from datetime import datetime
import random

DEFAULT_PHOTO = "default.jpg"

DEFAULT_PLACES = [
    {
        "name": "Парк Наталка",
        "type": "парк",
        "location": "Київ",
        "description": "Затишний парк для прогулянок та відпочинку.",
        "rating": 5,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "photo": DEFAULT_PHOTO
    },
    {
        "name": "Pinchuk Art Centre",
        "type": "арт-центр",
        "location": "Київ",
        "description": "Сучасний арт-центр з виставками сучасного мистецтва.",
        "rating": 5,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "photo": DEFAULT_PHOTO
    },
    {
        "name": "Театр Лесі Українки",
        "type": "театр",
        "location": "Київ",
        "description": "Відомий театр з різноманітними постановками.",
        "rating": 5,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "photo": DEFAULT_PHOTO
    }
]

def get_places(request):
    if "places" not in request.session:
        request.session["places"] = DEFAULT_PLACES.copy()
    return request.session.get("places", [])

def save_places(request, places):
    request.session["places"] = places

def index(request):
    get_places(request)
    return render(request, "index.html")

def places_list(request):
    places = get_places(request)
    return render(request, "places_list.html", {"places": places})

def random_place(request):
    places = get_places(request)

    weighted = []
    for place in places:
        weighted += [place] * int(place.get("rating", 1))

    chosen = random.choice(weighted) if weighted else None
    return render(request, "random_place.html", {"place": chosen})

def add_place(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        type_ = request.POST.get("type")
        location = request.POST.get("location") or None
        description = request.POST.get("description")
        rating = request.POST.get("rating")

        if not name or not description or not rating:
            error = "Заповніть усі поля."
        elif not rating.isdigit() or not (1 <= int(rating) <= 5):
            error = "Рейтинг має бути числом від 1 до 5."
        else:
            places = get_places(request)
            places.append({
                "name": name,
                "type": type_,
                "location": location,
                "description": description,
                "rating": int(rating),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "photo": DEFAULT_PHOTO
            })
            save_places(request, places)
            return redirect("places_list")

    return render(request, "add_place.html", {"error": error})

def place_detail(request, index):
    places = get_places(request)
    if 0 <= index < len(places):
        return render(request, "place_detail.html", {"place": places[index]})
    return redirect("places_list")

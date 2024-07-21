from django.shortcuts import render

# Create your views here.
def placesListMap(request):
    return render(request, 'p1frontend/places_base.html')

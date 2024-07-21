from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Place

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello Worldlings, greetigns from planet kosnoztik, We come in peace , hahhaha!')

def all_places(request):
    queryset = Place.objects.all()
    print(queryset)
    geojsonquery = serialize('geojson', queryset, geometry_field='point_geom', srid=3857)
    return HttpResponse(geojsonquery, content_type='application/json')

def place_detail(request, rk):
    data = []
    try:
        place = Place.objects.get(pk=rk)
        data.append(place)
    except Place.DoesNotExist:
        pass

    # Pass data if place ID exists, else pass null data 
    geojsonsingleqbyid = serialize('geojson', data, geometry_field = 'point_geom', srid = 3857)
    return HttpResponse(geojsonsingleqbyid, content_type='application/json' )
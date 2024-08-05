from .models import Place, Category, City, Contact
from .serializers import CategorySerializer, PlaceSerializer, CitySerializer, ContactSerializer
from rest_framework import generics,viewsets

from django.http import Http404
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

# Note that with the filter, whichever places that are clicked as Active (in checkbox in pgadmin) will be shown. So it is a tool to stop certain ads from being shown.
class PlaceList(generics.ListAPIView):
    queryset = Place.objects.filter(active=True)
    serializer_class = PlaceSerializer
    name = 'places-list'

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.filter(active=True)
    serializer_class = PlaceSerializer
    name = 'places-detail'

class CityList(generics.ListAPIView):
    serializer_class = CitySerializer
    name = 'cities-list'

    # queryset function is being overriden in this class
    def get_queryset(self):
        placeID = self.request.GET.get('placeid')

        if placeID is None:
            raise Http404("Place ID parameter is missing")
        
        try:     
            selectedPlace = get_object_or_404(Place, pk=placeID)
        except Place.DoesNotExist:
            raise Http404("Place not found")
        
        selectedPlaceGeom = selectedPlace.point_geom
        nearestCities = City.objects.annotate(distance=Distance('wkb_geometry', selectedPlaceGeom)).order_by('distance')[:4]
        return nearestCities
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'contact-list'


    
from rest_framework import generics

from .models import Beer
from .serializers import BeerSerializer

#this view takes cares of both creating and listing data in db
class BeerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class BeerDetailAPIView(generics.RetrieveAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


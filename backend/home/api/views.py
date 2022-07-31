from rest_framework.response import Response
from rest_framework.decorators import api_view

from beers.models import Beer
from beers.serializers import BeerSerializer

@api_view(['GET']) #decorator makes it into an DRF API view, where I declared only GET requests are allowed
def api_home(request, *args, **kwargs):
    instance = Beer.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = BeerSerializer(instance).data
    return Response(data)
from rest_framework.response import Response
from rest_framework.decorators import api_view

from beers.models import Beer
from beers.serializers import BeerSerializer

@api_view(['POST']) #decorator makes it into an DRF API view, where I declared only GET requests are allowed
def api_home(request, *args, **kwargs):
    instance = Beer.objects.all().order_by('?').first()
    data = {}
    serializer = BeerSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
    return Response(data)

    
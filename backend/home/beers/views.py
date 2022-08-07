from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Beer
from .serializers import BeerSerializer, BeerUpdateSerializer


class BeerMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, args, kwargs)

        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)



#this view takes cares of both creating and listing data in db
class BeerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAuthenticated] #Describes who has permission to do what on the given view

    def perform_create(self, serializer):
        print("We are creating now")
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = 'No description for this Beer'
        instance = serializer.save(description = description)
        print(instance)

class BeerDetailAPIView(generics.RetrieveAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class BeerUpdateAPIView(generics.UpdateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerUpdateSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        print("Updating")
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.name
            #instance.save()


class BeerDeleteAPIView(generics.DestroyAPIView):
    queryset = Beer.objects.all()
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

@api_view(['GET','POST'])
def beers_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if pk is not None:
        obj = get_object_or_404(Beer, pk=pk)
        data = BeerSerializer(obj, many=False).data
        return Response(data)
    
    if method == 'GET':
        queryset = Beer.objects.all()
        data = BeerSerializer(queryset, many=True).data
        return Response(data)
    elif method =='POST':
        serializer = BeerSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": "Data given not valid"}, status=400)
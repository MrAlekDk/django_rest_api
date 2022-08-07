from rest_framework import serializers

from .models import Beer

#Serializer for my Beer model, using Meta will generate the fields for the serializer automatically 
class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields=[
            'name',
            'beer_type',
            'description',
            'price',
            'sale_price'
        ]

#Serializer made for the UpdateView, so that any field can be changed and no 'required' exceptions are raised
class BeerUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=25, required = False)
    beer_type = serializers.CharField(max_length=25, required = False)
    description = serializers.CharField(max_length=250, required = False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, default=44.44, required = False)
    class Meta:
        model = Beer
        fields=[
            'name',
            'beer_type',
            'description',
            'price',
            'sale_price'
        ]
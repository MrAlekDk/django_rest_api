from rest_framework import serializers

from .models import Beer

#Serializer for my Beer model
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
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hotels
from .serializers import HotelSeriailzers

@api_view(['GET', 'POST'])
def HotelList(request):
    if request.method == 'GET':
        hotelList = Hotels.objects.all()
        hotelSerializer = HotelSeriailzers(hotelList, many=True)
        return Response(hotelSerializer.data)
    if request.method == 'POST':
        hotelRequest = request.data
        serializeData = HotelSeriailzers(data=hotelRequest)
        if serializeData.is_valid():
            serializeData.save()

        return Response({"Message": "Saved successfully"})

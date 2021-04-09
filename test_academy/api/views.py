from django.db.models import Sum, F
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(('GET',))
def total_cost(request):
    """
    :return: sum of multiplying price by amount for all products in db
    """
    return Response({'total_cost': Product.objects.all().aggregate(sum=Sum(F('price')*F('amount')))["sum"]})

from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from rest_framework.response import Response

@api_view(["POST"])
def api_home(request, *args, **keargs):
    """
    DRF API VIEW
    """
    
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertyListSerializer

class PropertyListView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertyListSerializer({"data": properties})
        return Response(serializer.data)

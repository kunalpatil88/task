from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertyListSerializer

# class PropertyListView(APIView):
#     def post(self, request):
#         properties = Property.objects.all()
#         serializer = PropertyListSerializer({"data": properties})
#         return Response(serializer.data)
    

# class PropertyListView(APIView, PageNumberPagination):
#     page_size = 5
#     def post(self, request):
#         try:
#             properties = Property.objects.all()
#             results = self.paginate_queryset(properties, request, view=self)
#             serializer=PropertyListView(results,many=True,context={'request':properties})
#             return Response({"status": "success", "message": self.get_paginated_response(serializer.data).data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# class PropertyListView(APIView):
#     def post(self, request):
#         limit = request.query_params.get('limit')
#         offset = request.query_params.get('offset')
        # category_limit = request.query_params.get('category_limit')  # Get the category_limit from query parameters

        # Validate limit and offset parameters
        # try:
        #     limit = int(limit) if limit else None
        # except ValueError:
        #     return Response({"error": "Invalid 'limit' parameter"}, status=status.HTTP_400_BAD_REQUEST)
########################
        # try:
        #     offset = int(offset) if offset else None
        # except ValueError:
        #     return Response({"error": "Invalid 'offset' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     limit = int(limit) if limit else None
        # except ValueError:
        #     return Response({"error": "Invalid 'limit' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # serializer = PropertyListSerializer(data={"limit": limit, "offset": offset, "limit": limit})
        # if serializer.is_valid():
        #     data = serializer.data
        #     return Response(data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class PropertyListView(APIView):
    def post(self, request):
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        # Validate limit and offset parameters
        try:
            limit = int(limit) if limit else None
        except ValueError:
            return Response({"error": "Invalid 'limit' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            offset = int(offset) if offset else None
        except ValueError:
            return Response({"error": "Invalid 'offset' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PropertyListSerializer(data={"limit": limit, "offset": offset})
        if serializer.is_valid():
            data = serializer.data
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer

@api_view(['POST'])
def create_short_url(request):
    """
    Create a new short URL.
    Expects 'original_url' in the request data.
    """
    serializer = URLSerializer(data=request.data)
    if serializer.is_valid():
        # Save the URL and automatically generate a short code
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

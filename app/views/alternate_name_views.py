from django.http import JsonResponse
from app.models.test import AlternateName
from ..serializers import AlternateNameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .views_helper import validate_model

@api_view(['GET'])
def AlternateNameList(request, format=None):

    if request.method == 'GET':
        alternatenames = AlternateName.objects.all().order_by('name')
        serializer = AlternateNameSerializer(alternatenames, many=True)
        return JsonResponse({'alternatenames':serializer.data}, safe=False)

@api_view(['GET'])
def AlternateNameDetail(request, id, format=None):

    alternatenames, error_response = validate_model(AlternateName, id)

    if error_response:
        return error_response

    if request.method == 'GET':
        serializer = AlternateNameSerializer(alternatenames)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
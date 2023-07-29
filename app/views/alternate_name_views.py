from django.http import JsonResponse
from app.models.test import AlternateName
from ..serializers import AlternateNameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def AlternateNameList(request, format=None):

    if request.method == 'GET':
        alternatenames = AlternateName.objects.all()
        serializer = AlternateNameSerializer(alternatenames, many=True)
        return JsonResponse({'alternatenames':serializer.data}, safe=False)

@api_view(['GET'])
def AlternateNameDetail(request, id, format=None):

    try:
        alternatenames = AlternateName.objects.get(pk=id)
    except AlternateName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlternateNameSerializer(alternatenames)
        return Response(serializer.data)
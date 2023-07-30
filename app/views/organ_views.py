from django.http import JsonResponse
from app.models.organ import Organ
from ..serializers import OrganSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .views_helper import validate_model

@api_view(['GET'])
def OrganList(request, format=None):

    if request.method == 'GET':
        organs = Organ.objects.all()
        serializer = OrganSerializer(organs, many=True)
        return JsonResponse({'organs':serializer.data}, safe=False)

@api_view(['GET'])
def OrganDetail(request, id, format=None):
    organs, error_response = validate_model(Organ, id)

    if error_response:
        return error_response

    if request.method == 'GET':
        serializer = OrganSerializer(organs)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
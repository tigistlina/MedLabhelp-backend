from django.http import JsonResponse
from app.models.test import Test, AlternateName
from app.models.panel import Panel
from ..serializers import TestSerializer, AlternateNameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .views_helper import validate_model

@api_view(['GET'])
def TestList(request, format=None):

    if request.method == 'GET':
        tests = Test.objects.all().order_by('name')
        serializer = TestSerializer(tests, many=True)
        return JsonResponse({'tests':serializer.data}, safe=False)

@api_view(['GET'])
def TestDetail(request, id, format=None):

    tests, error_response = validate_model(Test, id)

    if error_response:
        return error_response

    if request.method == 'GET':
        serializer = TestSerializer(tests)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def AltNameFromTest(request, id, format=None):
    test, error_response = validate_model(Test, id)

    if error_response:
        return error_response
    
    if request.method == 'GET':
        alternate_name = AlternateName.objects.filter(test_id=test.id).order_by('name')
        serializer = AlternateNameSerializer(alternate_name, many= True)
        return Response(serializer.data)
    
    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



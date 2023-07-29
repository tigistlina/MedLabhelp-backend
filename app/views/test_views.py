from django.http import JsonResponse
from app.models.test import Test
from ..serializers import TestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def TestList(request, format=None):

    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return JsonResponse({'tests':serializer.data}, safe=False)

@api_view(['GET'])
def TestDetail(request, id, format=None):

    try:
        tests = Test.objects.get(pk=id)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestSerializer(tests)
        return Response(serializer.data)
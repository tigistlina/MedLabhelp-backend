from django.http import JsonResponse
from app.models.organ import Organ
from app.models.panel import Panel
from app.models.test import Test
from ..serializers import OrganSerializer , TestSerializer
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

@api_view(['GET'])
def TestDetailByOrganId(request, id, format=None):
    organs, error_response = validate_model(Organ, id)

    if error_response:
        return error_response

        # first we are going to query for all panels associated with the argan which will give us a list of panel ids
        # then query for all test associated with those panel ids
        # we can serialize those tests and return the test
    if request.method == 'GET':
        panels = Panel.objects.filter(organ_id=id)
        panel_ids = [panel.id for panel in panels]

        tests = Test.objects.filter(panel_id__in=panel_ids)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
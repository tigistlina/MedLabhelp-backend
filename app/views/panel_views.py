from django.http import JsonResponse
from app.models.panel import Panel
from app.models.test import Test
from ..serializers import PanelSerializer, TestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .views_helper import validate_model

@api_view(['GET'])
def PanelList(request, format=None):

    if request.method == 'GET':
        panels = Panel.objects.all().order_by('name')
        serializer = PanelSerializer(panels, many=True)
        return JsonResponse({'panels':serializer.data}, safe=False)

@api_view(['GET'])
def PanelDetail(request, id, format=None):

    panels, error_response = validate_model(Panel, id)

    if error_response:
        return error_response

    if request.method == 'GET':
        serializer = PanelSerializer(panels)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def TestToPanel(request, id, format=None):
    panels, error_response = validate_model(Panel, id)

    if error_response:
        return error_response

    if request.method == 'GET' :
        tests = Test.objects.filter(panel_id=panels.id).order_by('name')
        serializer = TestSerializer(tests, many= True)
        return Response(serializer.data)

    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
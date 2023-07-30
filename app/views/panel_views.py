from django.http import JsonResponse
from app.models.panel import Panel
from ..serializers import PanelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .views_helper import validate_model

@api_view(['GET'])
def PanelList(request, format=None):

    if request.method == 'GET':
        panels = Panel.objects.all()
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
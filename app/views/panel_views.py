from django.http import JsonResponse
from app.models.panel import Panel
from ..serializers import PanelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def PanelList(request, format=None):

    if request.method == 'GET':
        panels = Panel.objects.all()
        serializer = PanelSerializer(panels, many=True)
        return JsonResponse({'panels':serializer.data}, safe=False)

@api_view(['GET'])
def PanelDetail(request, id, format=None):

    try:
        panels = Panel.objects.get(pk=id)
    except Panel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PanelSerializer(panels)
        return Response(serializer.data)
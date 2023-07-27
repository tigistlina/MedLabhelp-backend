from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from app.models import Test , TestSerializer
# Create your views here.
class TestList(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class TestDetail(APIView):
    def get(self,request,id):
        pass
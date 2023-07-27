from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# from main.models import Book, BookSerializer....need to update to reflect our model

# Create your views here.
# class BookList(APIView): ....need to update to reflect our model
    def get(self, request):
        # books = Book.objects.all()...need 
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
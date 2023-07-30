from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def validate_model(cls, model_id):
    try:
        int_model_id = int(model_id)
    except ValueError:
        return None, JsonResponse({'error': f"Invalid ID format. Please provide a valid integer ID for {cls.__name__}."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        model = cls.objects.get(pk=int_model_id)
    except cls.DoesNotExist:
        return None, JsonResponse({'error': f"{cls.__name__} with ID {int_model_id} not found."}, status=status.HTTP_404_NOT_FOUND)

    return model, None
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def validate_model(cls,model_id):
    try:
        int_model_id = int(model_id)
    except ValueError:
        return JsonResponse(f"{cls.__name__} with id {model_id} does not exist.",safe=False)

    try:
        model = cls.objects.get(pk=int_model_id)
    except cls.DoesNotExist:
        return JsonResponse({"message":f"{cls.__name__} {int_model_id} not found"}, 404)

    return model
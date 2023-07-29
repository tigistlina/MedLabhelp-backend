from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def validate_model(cls,model_id):
    try:
        model_id = int(model_id)
    except ObjectDoesNotExist:
        return JsonResponse(f"Test with id {model_id} does not exist.",safe=False)
        
    model = cls.query.get(model_id)

    if not model:
        return JsonResponse({"message":f"{cls.__name__} {model_id} not found"}, 404)

    return model
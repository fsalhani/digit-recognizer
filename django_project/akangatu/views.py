from django.http import JsonResponse, HttpResponseNotAllowed
from django_quicky import routing
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Predictor

# flask-style route decorators
url, urlpatterns = routing()

predictor_acessor = Predictor()

@url(r'^health_check/king$')
def king(request):
    if request.method.upper() != 'GET':
        return HttpResponseNotAllowed(['GET'])  # List of allowed ones
    else:
        return JsonResponse({
            'message': 'Dani Delícia!!!',
        }, status=200)

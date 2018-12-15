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

@url(r'^predict$')
@csrf_exempt
def predict(request):
    if request.method.upper() != 'POST':
        return HttpResponseNotAllowed(['POST'])  # List of allowed ones

    json_data = request.POST.dict() or json.loads(request.body.decode('utf-8'))

    print(json_data)

    pred = predictor_acessor.predict(json_data['pixels'])

    answer = {'label': int(pred[0]) }

    return JsonResponse(answer, safe=False, status=200)

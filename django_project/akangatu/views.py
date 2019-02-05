from django.http import JsonResponse, HttpResponseNotAllowed
from django_quicky import routing
from django.views.decorators.csrf import csrf_exempt
import json
import matplotlib.image as img

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
            'message': 'kong',
        }, status=200)

@url(r'^predict$')
@csrf_exempt
def predict(request):
    if request.method.upper() != 'POST':
        return HttpResponseNotAllowed(['POST'])  # List of allowed ones

    image_file = next(iter(request.FILES.values()))

    image = img.imread(image_file)

    pred = predictor_acessor.predict(image)

    answer = {'label': int(pred[0]) }

    return JsonResponse(answer, safe=False, status=200)

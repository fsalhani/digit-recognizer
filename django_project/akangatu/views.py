from django.http import JsonResponse, HttpResponseNotAllowed
from django_quicky import routing

# flask-style route decorators
url, urlpatterns = routing()

@url(r'^health_check/king$')
def king(request):
    if request.method.upper() != 'GET':
        return HttpResponseNotAllowed(['GET'])  # List of allowed ones
    else:
        return JsonResponse({
            'message': 'Dani Delícia!!!',
        }, status=200)

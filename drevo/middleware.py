from django.http import HttpResponse

class DrevoInit:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        print('Initialyzing knowledge tree ...')
        response = self._get_response(request)
        return response
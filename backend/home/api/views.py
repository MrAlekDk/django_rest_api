from django.http import JsonResponse


def api_home(req, *args, **kwargs):
    return JsonResponse({'message': 'A Django API response in JSON format'})
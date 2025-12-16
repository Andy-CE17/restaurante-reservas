from django.shortcuts import render
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({
        'mensaje': "hola React , Django esta vivo "
    })

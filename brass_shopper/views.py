from django.shortcuts import render

def brass_shopper_func(request, **kwargs):
    return render(request, 'brass_shopper/index.html', {})

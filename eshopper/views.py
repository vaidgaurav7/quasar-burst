from django.shortcuts import render

def eshopper_func(request, **kwargs):
    return render(request, 'eshopper/index.html', {})

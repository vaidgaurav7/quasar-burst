from django.shortcuts import render

def portfolio_func(request, **kwargs):
    return render(request, 'portfolio/index.html', {})

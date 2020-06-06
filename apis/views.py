from django.shortcuts import render
from apis.models import TiLoginUserData2
from .serializers import TiLoginUserData2Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse ,JsonResponse

@api_view(['GET'])
def user_id_func(request, **kwargs):
    if request.method == 'GET':
        data = TiLoginUserData2.objects.all()
        serializer = TiLoginUserData2Serializer(data, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def parte_user_id_func(request, pk):
    if request.method == 'GET':
        data = None
        try:
            data = TiLoginUserData2.objects.get(pk=pk)
        except Exception as e:
            return JsonResponse({'MESSAGE' : 'Invalid Request'})
        print(data)
        serializer = TiLoginUserData2Serializer(data)
        return Response(serializer.data)

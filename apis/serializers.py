from apis.models import TiLoginUserData2
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class TiLoginUserData2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TiLoginUserData2
        fields = ['user_id','password','mark_attandance']

class TiLoginUserData2SerializerViewSet(viewsets.ModelViewSet):
    queryset = TiLoginUserData2.objects.all()
    serializer_class = TiLoginUserData2Serializer

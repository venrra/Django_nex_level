from rest_framework.serializers import ModelSerializer
from ouruser.models import User


class UserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'name',
            'surname'
        ]
        read_only_fields = [
            'id',
        ]

from drf_yasg.utils import swagger_auto_schema

from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_yasg import openapi

from ouruser.serializers import UserSerializer
from ouruser.models import User

class UserView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    system_log = "User"

    username = openapi.Parameter(
        "username",
        openapi.IN_QUERY,
        description="username",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        responses={status.HTTP_404_NOT_FOUND: "Not found"},
        manual_parameters=[username],
    )
    @action(methods=["get"], detail=False)
    def find_by_name(self, request, *args, **kwargs):
        username = request.GET.get('username', None)
        if username is not None:
            try:
                user = self.queryset.get(username=username)
                data = self.serializer_class(user).data
                return Response(data=data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"error": f"The user {username} not found"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "The param username is required"})




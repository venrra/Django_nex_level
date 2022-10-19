# Django classic imports
from django.urls import re_path, include

# Swagger and DRF imports
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views import
from ouruser import views as user_views

# Schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router = routers.DefaultRouter()

router.register(
   "user",
   user_views.UserView,
   basename="user"
)

urlpatterns += [
   re_path(r"^services/", include((router.urls, "v1"), namespace="v1"))
]

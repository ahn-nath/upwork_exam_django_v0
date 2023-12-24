from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from users_app import views

# TODO: update it
schema_view = get_schema_view(
    openapi.Info(
        title="Users API",
        default_version='v1',
        description="Test description",
        terms_of_service="",
        contact=openapi.Contact(email="nathaly12toledo@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', schema_view),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Point DRF docs to root path

]

urlpatterns += router.urls

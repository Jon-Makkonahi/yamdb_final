from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
    openapi.Info(
      title="Api_yamdb API",
      default_version='v1',
      description="Документация  проекта api_yamdb",
      contact=openapi.Contact(email="admin@api_yamdb.ru"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'),
]

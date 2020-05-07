from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'common_diseases', views.CommonDiseasesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-path/', include('rest_framework.urls', namespace='rest_framework'))
]

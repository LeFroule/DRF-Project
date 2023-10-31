from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from cars.views import *
from rest_framework import routers
from .myrouters import MyCustomRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/cars/', CarsAPIList.as_view()),
    path('api/v1/cars/<int:pk>/', CarsAPIUpdate.as_view()),
    path('api/v1/carsdelete/<int:pk>', CarsAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]


# router = MyCustomRouter()
# router.register(r'cars', CarsViewSet, basename='cars')
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls))
# ]

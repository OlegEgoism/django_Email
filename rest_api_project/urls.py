"""rest_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from accaunt.views import SimpleApI
from api.views import get_presente, all_shop, all_mag, Magazik
from reactdjango.views import CarViewSet
from stas_class.views import ZawodList, CreateZawod, ZawodDetail, StartViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'zawod', ZawodDetail)
router.register(r'maga', Magazik, basename='magaz')
router.register(r'start', StartViewSet)
urlpat = router.urls
router.register(r'car', CarViewSet, basename='car')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello', SimpleApI.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('accaunt/', include('accaunt.urls')),
    path('svazi/', include('svazi.urls')),

    # path('presente/', get_presente, name='presente'),
    # path('shop/<int:id>', all_shop, name='all_shop'),
    # path('mag/',all_mag),
    # path('zawod/', ZawodList.as_view()),
    # path('zaw/', CreateZawod.as_view())
    # path('prod/',)
    *urlpat,


]
urlpatterns +=router.urls
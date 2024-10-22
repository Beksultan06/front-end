from rest_framework.routers import DefaultRouter

from .views import SettingsAPI

router = DefaultRouter()
router.register('test', SettingsAPI, basename="test API")

urlpatterns = [
    
]

urlpatterns += router.urls
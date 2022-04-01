from django.urls import path
from rest_framework import routers
from .views import ShowViewset, userViewset

router = routers.DefaultRouter()
router.register(r'users', userViewset)
router.register(r'shows', ShowViewset)


urlpatterns = router.urls
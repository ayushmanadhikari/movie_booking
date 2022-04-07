from django.urls import path
from rest_framework import routers
from .views import BookedViewset, ShowViewset

router = routers.DefaultRouter()
router.register(r'shows', ShowViewset)
router.register(r'booked', BookedViewset)


urlpatterns = router.urls
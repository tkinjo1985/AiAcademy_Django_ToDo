from rest_framework import routers
from .views import ToDoViewSet

router = routers.DefaultRouter()
router.register('entries', ToDoViewSet, basename='todo')
urlpatterns = router.urls

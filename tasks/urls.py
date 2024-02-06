from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api/tasks', views.TaskViewSet, basename="tasks")
urlpatterns = router.urls

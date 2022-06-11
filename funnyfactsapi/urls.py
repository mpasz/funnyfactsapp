from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('dates', views.FunnyFactsViewSet, basename="list")
router.register('popular', views.PopularFunnyFactViewSet, basename="popular-facts-list")


urlpatterns = (
    router.urls
)



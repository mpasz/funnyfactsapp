from django.urls import path
from funnyfactsapi.views import (
    funny_fact_list,
    funny_fact_detail
)

app_name = 'funny_fact'

urlpatterns = [
    path('dates/', funny_fact_list, name='list'),
    path('dates/<int:id>/', funny_fact_detail, name='detail'),
]


# router = routers.DefaultRouter()
# router.register('dates', views.FunnyFactsViewSet, basename="list")
# router.register('popular', views.PopularFunnyFactViewSet, basename="popular-facts-list")


# urlpatterns = (
#     router.urls
# )



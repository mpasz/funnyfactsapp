from django.urls import path
from funnyfactsapi.views import (
    FunnyFactDetail,
    FunnyFactsList,
    # funny_fact_list,
    # funny_fact_detail
)

app_name = 'funny_fact'

urlpatterns = [
    path('dates/', FunnyFactsList.as_view()),
    path('dates/<int:pk>/', FunnyFactDetail.as_view()),
]


# router = routers.DefaultRouter()
# router.register('dates', views.FunnyFactsViewSet, basename="list")
# router.register('popular', views.PopularFunnyFactViewSet, basename="popular-facts-list")


# urlpatterns = (
#     router.urls
# )



from django.urls import path
from funnyfactsapi.views import (
    FunnyFactDetail,
    FunnyFactsList,
    PopularFunyFacts
)

app_name = 'funny_fact'

urlpatterns = [
    path('dates/', FunnyFactsList.as_view()),
    path('dates/<int:pk>/', FunnyFactDetail.as_view()),
    path('popular/', PopularFunyFacts.as_view())
]

from django.conf import settings
from .models import FunnyFacts
from .services import get_funny_fact
from .serializers import FunnyFactSerializer, PopularFunnyFactSerializer, SaveFunnyFactSerializer
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from funnyfactsapi import serializers


class FunnyFactsViewSet(ModelViewSet):
    
    serializer_class = FunnyFactSerializer
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return FunnyFacts.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveFunnyFactSerializer
        else:
            return FunnyFactSerializer

    def retrieve(self, request, pk):
        queryset = FunnyFacts.objects.all()
        fact = get_object_or_404(queryset, id=pk)

        serializer = FunnyFactSerializer(fact)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        day = request.data['day']
        month = request.data['month']
        daymonth = str(day) + str(month)
        fact = get_funny_fact(day, month)

        valid_days = {'1','2','3','4','5','6','7','8','9','10',
                      '11','12','13','14','15','16','17','18','19','20',
                      '21','22','23','24','25','26','27','28','29','30','31'}
        valid_months = {'1','2','3','4','5','6','7','8','9','10','11','12'}

        if (day in valid_days) and (month in valid_months):
            try:
                new_fact = FunnyFacts.objects.create(day=day, month=month, daymonth=daymonth, fact=fact)
                new_fact.save()
                serializer = SaveFunnyFactSerializer(new_fact)
                obj_id = serializer.data['id']
                return redirect(f'{request.stream.path}{obj_id}')
            except :
                queryset = FunnyFacts.objects.all()
                db_fact = get_object_or_404(queryset, daymonth=daymonth)
                if db_fact.fact != fact:
                    db_fact.fact = fact
                    db_fact.save()
                    serializer = SaveFunnyFactSerializer(db_fact)
                    obj_id = serializer.data['id']
                    return redirect(f'{request.stream.path}{obj_id}')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            # return Response("Pass the valid day and month value")

    def destroy(self, request, pk):
        token = settings.X_API_TOKEN
        key = request.query_params.get('X-API-KEY')
        if key:
            if token == request.query_params['X-API-KEY']:
                fact = get_object_or_404(FunnyFacts, pk=pk)
                fact.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
   
class PopularFunnyFactViewSet(ModelViewSet):

    serializer_class = PopularFunnyFactSerializer
    http_method_names = ["get"]
    
    def get_queryset(self):
        result = (FunnyFacts.objects
                .values('month')
                .annotate(days_checked=Count('day'))
                .order_by()
                )
        return result
   

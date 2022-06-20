from django.db.models.aggregates import Count
from django.shortcuts import (
    get_object_or_404, 
    redirect
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from funnyfactsapp.settings import dev
from funnyfactsapi.models import FunnyFacts
from funnyfactsapi.services import get_funny_fact
from funnyfactsapi.serializers import (
    FFSerializer,
    PopularFunnyFactSerializer, 
    SaveFunnyFactSerializer
)
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveDestroyAPIView, 
    ListAPIView
)


class FunnyFactsList(ListCreateAPIView):
    def get_queryset(self):
        return FunnyFacts.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FFSerializer
        elif self.request.method == 'POST':
            return SaveFunnyFactSerializer

    def create(self, request, *args, **kwargs):
        day=request.data['day']
        month = request.data['month']
        daymonth = str(day) + str(month)
        fact = get_funny_fact(day, month)

        if day in list(range(1,31)) and month in list(range(1,12)):
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
            return Response({'error': 'Given day or month is out of range'}, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        return {'request': self.request}


class FunnyFactDetail(RetrieveDestroyAPIView):
    
    def get_queryset(self):
        return FunnyFacts.objects.all() 

    def get_serializer_class(self):
        return FFSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
    def delete(self, request, pk):
        token = dev.X_API_KEY
        key = request.query_params.get('X-API-KEY')
        if key:
            if token == request.query_params['X-API-TOKEN']:
                fact = get_object_or_404(FunnyFacts, pk=pk)
                fact.delete()
                return Response({'message':'Object has been deleted'},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error':'Invalid value of secret key'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error' : 'You should provide secret key to delete object'}, status=status.HTTP_403_FORBIDDEN)
    

class PopularFunyFacts(ListAPIView):
    
    def get_queryset(self):
        return (FunnyFacts.objects
                .values('month')
                .annotate(days_checked=Count('day'))
                .order_by()
                )
    
    def get_serializer_class(self):
        return PopularFunnyFactSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    

# from funnyfactsapi import serializers


# class FunnyFactsViewSet(ModelViewSet):
    
#     serializer_class = FunnyFactSerializer
#     http_method_names = ["get", "post", "delete"]

#     def get_queryset(self):
#         return FunnyFacts.objects.all()

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return SaveFunnyFactSerializer
#         else:
#             return FunnyFactSerializer

#     def retrieve(self, request, pk):
#         queryset = FunnyFacts.objects.all()
#         fact = get_object_or_404(queryset, id=pk)

#         serializer = FunnyFactSerializer(fact)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         day = request.data['day']
#         month = request.data['month']
#         daymonth = str(day) + str(month)
#         fact = get_funny_fact(day, month)

#         valid_days = {'1','2','3','4','5','6','7','8','9','10',
#                       '11','12','13','14','15','16','17','18','19','20',
#                       '21','22','23','24','25','26','27','28','29','30','31'}
#         valid_months = {'1','2','3','4','5','6','7','8','9','10','11','12'}

#         if (day in valid_days) and (month in valid_months):
#             try:
#                 new_fact = FunnyFacts.objects.create(day=day, month=month, daymonth=daymonth, fact=fact)
#                 new_fact.save()
#                 serializer = SaveFunnyFactSerializer(new_fact)
#                 obj_id = serializer.data['id']
#                 return redirect(f'{request.stream.path}{obj_id}')
#             except :
#                 queryset = FunnyFacts.objects.all()
#                 db_fact = get_object_or_404(queryset, daymonth=daymonth)
#                 if db_fact.fact != fact:
#                     db_fact.fact = fact
#                     db_fact.save()
#                     serializer = SaveFunnyFactSerializer(db_fact)
#                     obj_id = serializer.data['id']
#                     return redirect(f'{request.stream.path}{obj_id}')
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#             # return Response("Pass the valid day and month value")

#     def destroy(self, request, pk):
#         token = settings.X_API_TOKEN
#         key = request.query_params.get('X-API-KEY')
#         if key:
#             if token == request.query_params['X-API-KEY']:
#                 fact = get_object_or_404(FunnyFacts, pk=pk)
#                 fact.delete()
#                 return Response(status=status.HTTP_204_NO_CONTENT)
#             else:
#                 return Response(status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(status.HTTP_404_NOT_FOUND)
   
# class PopularFunnyFactViewSet(ModelViewSet):

#     serializer_class = PopularFunnyFactSerializer
#     http_method_names = ["get"]
    
#     def get_queryset(self):
#         result = (FunnyFacts.objects
#                 .values('month')
#                 .annotate(days_checked=Count('day'))
#                 .order_by()
#                 )
#         return result
   

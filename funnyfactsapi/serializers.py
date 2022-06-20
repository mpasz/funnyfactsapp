import calendar
from funnyfactsapi.services import get_funny_fact
from .models import FunnyFacts
from rest_framework import serializers



class FunnyFactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    month = serializers.SerializerMethodField(method_name='_get_month_name')
   
    class Meta:
        model = FunnyFacts
        fields = ['id', 'day','month', 'fact']    
    
    def _get_month_name(self, obj):
        return calendar.month_name[obj.month]

class SaveFunnyFactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    fact = serializers.CharField(read_only = True)
    # month = serializers.SerializerMethodField('_get_month_name')
    class Meta:
        model = FunnyFacts
        fields = [ 'id','day', 'month', 'fact']
    
    def _get_month_name(self, obj):
        return calendar.month_name[obj.month]
    
    def create(self, validated_data):
        funny_fact = FunnyFacts(**validated_data)
        funny_fact.daymonth = str(validated_data['day']) + str(validated_data['month'])
        funny_fact.fact = get_funny_fact(validated_data['day'], validated_data['month'])
        funny_fact.save()
        return funny_fact


class DeleteFunnyFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnyFacts
        fields = []

class UpdateFunnyFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnyFacts
        fields = ['fact']


class PopularFunnyFactSerializer(serializers.ModelSerializer):
    _id = 0
    days_checked = serializers.IntegerField()
    id = serializers.SerializerMethodField('_get_popular_id')
    class Meta:
        model = FunnyFacts
        fields = ['id', 'month', 'days_checked']

    def _get_popular_id(self, obj):
        self._id += 1
        return self._id



    


    
        
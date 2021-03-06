from rest_framework import serializers
from .models import *


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'created', 'name', 'describe', 'price', 'isDelete')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone', 'sex', 'location','identification', 'age', 'describe', 'agent')


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'describe', 'bReward','recommend')


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'college', 'phone')

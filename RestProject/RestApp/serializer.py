from rest_framework import serializers
from .models import Emp,Account,Singer,Songs
from django.contrib.auth.models import User

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'

# ****************************************************

class  UserSerializer(serializers.HyperlinkedModelSerializer):
    singer = serializers.PrimaryKeyRelatedField(many=True, queryset=Singer.objects.all())
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Songs.objects.all())

    class Meta:
        model=User
        fields=['url','username','email','singer','songs']

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Singer
        fields='__all__'

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields='__all__'
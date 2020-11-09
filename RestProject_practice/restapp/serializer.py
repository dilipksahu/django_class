from rest_framework import serializers
from .models import Emp,Account
 
# ModelSerializer - json format data define
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

# --------------- auth.User, Singer, Songs ---------------------
from .models import Singer,Songs
from django.contrib.auth.models import User

# HyperlinkedModelSerializer - url and primary key based data defines
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Singer and Songs Fields are not User table
    singer = serializers.PrimaryKeyRelatedField(many=True, queryset=Singer.objects.all())
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Songs.objects.all())
    class Meta:
        model = User
        fields = ['url','username','email','singer','songs']

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"
    
from rest_framework import serializers
from .models import Emp,Account

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
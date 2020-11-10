from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    class Meta:
        model = User
        fields = ['url','username','email','student']
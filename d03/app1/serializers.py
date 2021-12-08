from rest_framework import serializers
from .models import Student

class StudentSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
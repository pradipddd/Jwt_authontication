from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from .serializers import StudentSerializerModel
from .models import Student
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentCBV(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializerModel
    authentication_classes=[JWTTokenUserAuthentication]
    permission_classes=[IsAuthenticated]

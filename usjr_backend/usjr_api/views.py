from rest_framework import viewsets
from requests import Response
from . import models
from . import serializers

class CollegesViewSet(viewsets.ModelViewSet):
    queryset = models.Colleges.objects.all()
    serializer_class = serializers.CollegesSerializers

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = models.Departments.objects.all()
    serializer_class = serializers.DepartmentsSerializers

class ProgramsViewSet(viewsets.ModelViewSet):
    queryset = models.Programs.objects.all()
    serializer_class = serializers.ProgramsSerializers

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentsSerializers


from rest_framework import serializers
from . import models

class CollegesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Colleges
        fields = ('collid', 'collfullname', 'collshortname')

class DepartmentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = ('deptid', 'deptfullname', 'deptshortname', 'deptcollid')

class ProgramsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Programs
        fields = ('progid', 'progfullname', 'progshortname', 'progcollid', 'progcolldeptid')

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = ('studid', 'studfirstname', 'studlastname', 'studmidname', 'studprogid', 'studcollid', 'studyear')
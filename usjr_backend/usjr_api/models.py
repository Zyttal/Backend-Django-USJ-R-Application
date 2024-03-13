# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Colleges(models.Model):
    collid = models.IntegerField(primary_key=True)
    collfullname = models.CharField(max_length=100)
    collshortname = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'colleges'


class Departments(models.Model):
    deptid = models.IntegerField(primary_key=True)
    deptfullname = models.CharField(max_length=100)
    deptshortname = models.CharField(max_length=20, blank=True, null=True)
    deptcollid = models.ForeignKey(Colleges, models.DO_NOTHING, db_column='deptcollid')

    class Meta:
        managed = True
        db_table = 'departments'    


class Programs(models.Model):
    progid = models.IntegerField(primary_key=True)
    progfullname = models.CharField(max_length=100)
    progshortname = models.CharField(max_length=20, blank=True, null=True)
    progcollid = models.ForeignKey(Colleges, models.DO_NOTHING, db_column='progcollid')
    progcolldeptid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='progcolldeptid')

    class Meta:
        managed = True
        db_table = 'programs'


class Students(models.Model):
    studid = models.IntegerField(primary_key=True)
    studfirstname = models.CharField(max_length=50)
    studlastname = models.CharField(max_length=50)
    studmidname = models.CharField(max_length=50, blank=True, null=True)
    studprogid = models.IntegerField()
    studcollid = models.ForeignKey(Colleges, models.DO_NOTHING, db_column='studcollid')
    studyear = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'students'

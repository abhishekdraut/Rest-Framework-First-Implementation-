from django.db.models.fields import DateTimeField
from rest_framework import serializers
from rest_framework.fields import DateField


class blogseri(serializers.Serializer):

    title1 = serializers.CharField(max_length=10)
    description1=serializers.CharField(max_length=20)
    remark=serializers.CharField(max_length=255)
    date1=DateField()

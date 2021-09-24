from django.db.models.fields import DateTimeField
from rest_framework import serializers
from rest_framework.fields import DateField


class blog(serializers.Serializer):

    title = serializers.CharField(max_length=10)
    description=serializers.CharField(max_length=20)
    date=DateField()
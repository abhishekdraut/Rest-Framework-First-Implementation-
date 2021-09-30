from django.db.models import fields
from rest_framework.schemas.coreapi import field_to_schema
from api.models import blog
from django.db.models.fields import DateTimeField
from django.urls.conf import include
from rest_framework import serializers,routers
from rest_framework.fields import DateField



class blogseri(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields=['title', 'description' ,'date']

    # title = serializers.CharField(max_length=10)
    # description=serializers.CharField(max_length=20)
    # date=DateField()
    


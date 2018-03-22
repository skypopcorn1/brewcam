from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('created_at', 'image', 'pk')

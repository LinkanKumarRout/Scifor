from rest_framework import serializers
from .models import AllBlogs

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBlogs
        fields = "__all__"
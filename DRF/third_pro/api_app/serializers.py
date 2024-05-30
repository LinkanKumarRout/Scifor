from rest_framework import serializers

class PostSerializers(serializers.Serializer):
    userid = serializers.IntegerField()
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=200)
    body = serializers.CharField(max_length=200)
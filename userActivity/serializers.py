from .models import Post
from .models import Activity
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id','name', 'password')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('userId_id','login', 'logout','loginDuration')
    

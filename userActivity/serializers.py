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
        fields = ('userId','login', 'logout')
    # def create(self, data):
    #     post, __ = Post.objects.get_or_create(user_id=data["userId"])
    #     return Activity(logout=data["logout"], post=post)

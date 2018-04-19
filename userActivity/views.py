from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .models import Activity
from .serializers import UserSerializer
from .serializers import ActivitySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils import timezone
import json

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        incoming = data=request.data
        userIDValue = incoming["userId"]
        userDetails = Post.objects.get(name=incoming["name"])
        if userDetails.password == incoming["password"]:
            try:
                myActivity = Activity.objects.get(userId=userIDValue)
                #myActivity = get_object_or_404(Activity, userId=userIDValue)
            except Activity.DoesNotExist:
                serializer = ActivitySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            #myActivity = Activity.objects.get(userId=userIDValue)
            else:
                myActivity.login = timezone.now()
                myActivity.logout = None
                myActivity.save()
                return Response(status=status.HTTP_201_CREATED)
            # else:
            #     serializer = ActivitySerializer(data=request.data)
            #     if serializer.is_valid():
            #         serializer.save()
            #         return Response(serializer.data, status=status.HTTP_201_CREATED)
            #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def logout(request):
    if request.method == 'POST':
        incoming = data=request.data
        userIDValue = incoming["userId"]
        myActivity = Activity.objects.get(userId=userIDValue)
        loginTime = myActivity.login
        myActivity.logout=timezone.now()
        oldDiff = myActivity.loginDuration
        diff=timezone.now()-loginTime
        myActivity.loginDuration = diff.seconds + oldDiff
        myActivity.save()
        return Response(status=status.HTTP_201_CREATED)

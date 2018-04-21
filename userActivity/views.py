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
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def login(request):
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
        try:
            userDetails = Post.objects.get(name=incoming["name"])
        except Post.DoesNotExist:
            return JsonResponse({'message':'Username is invalid'})
        else:
            if userDetails.password == incoming["password"]:
                try:
                    myActivity = Activity.objects.get(userId_id=userIDValue)
                except Activity.DoesNotExist:
                    Activity(userId_id=userIDValue,logout=None).save()
                    return JsonResponse({'message':'Login Successful'})
                else:
                    myActivity.login = timezone.now()
                    myActivity.logout = None
                    myActivity.save()
                    return JsonResponse({'message':'Login Successful'})
            else:
                return JsonResponse({'message':'Password is invalid'})

@api_view(['GET', 'POST'])
def logout(request):
    if request.method == 'POST':
        incoming = data=request.data
        userIDValue = incoming["userId"]
        myActivity = Activity.objects.get(userId=userIDValue)
        loginTime = myActivity.login
        myActivity.logout=timezone.now()
        oldDiff = myActivity.loginDuration
        if oldDiff == None:
            oldDiff = 0
        diff=timezone.now()-loginTime
        myActivity.loginDuration = diff.seconds + oldDiff
        myActivity.save()
        return JsonResponse({'message':'Logout is Successful'})

@api_view(['GET','POST'])
def rankedUser(request):
    if request.method=='GET':
        allUserActivity = Activity.objects.order_by('-loginDuration')
        serializer = ActivitySerializer(allUserActivity,many=True)
        finalJsonArray = []
        for i,activityUser in enumerate(allUserActivity):
            userObject = Post.objects.get(user_id=activityUser.userId_id)
            userRankJson = {
                'id' : activityUser.userId_id,
                'name' : userObject.name,
                'lastlogin' : activityUser.login,
                'lastlogout' : activityUser.logout,
                'loginDuration' : activityUser.loginDuration,
                'rank':i+1
            }
            finalJsonArray.append(userRankJson)
        return JsonResponse(finalJsonArray,safe=False)

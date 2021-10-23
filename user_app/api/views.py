from rest_framework import status
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 

# from user_app import models    

from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def logout_view(request):
  if request.method == 'POST':
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration_view(request):
  if request.method == 'POST':
    serializer = RegistrationSerializer(data=request.data)

    newDict = {}
    if serializer.is_valid():
      account = serializer.save()
      newDict['username'] = account.username
      newDict['email'] = account.email
      #for token authentication

      # token = Token.objects.get(user = account).key
      # newDict['token'] = token
      refresh = RefreshToken.for_user(account)

      newDict['token'] = {
                          'refresh': str(refresh),
                          'access': str(refresh.access_token),
                      }



      newDict['response'] = "registration successful"

    else:
      newDict = serializer.errors

    return Response(newDict)

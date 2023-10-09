from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
# from serializer import UserSerializer
from .serializer import UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,'user': serializer.data}, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user=User.objects.all()
        user=list(user.values())
        return JsonResponse(data =user,status =200,safe = False)

        

class ScrapperViewset(generics.ListAPIView):
    def get(self,request):
        import ipdb;ipdb.set_trace()
        print('')
        return HttpResponse("this is get api")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
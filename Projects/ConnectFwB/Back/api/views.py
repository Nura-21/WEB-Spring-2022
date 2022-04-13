from django.http import JsonResponse
from django.shortcuts import render
from . models import User
from rest_framework import viewsets, permissions
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt




def index(request, path=''):
    return render(request, 'index.html')
 

class UserViewSet(APIView):
    @csrf_exempt
    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data, status=200)


class UserDetailAPIView(APIView):
    @csrf_exempt
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist as e:
            raise JsonResponse({f'message : {str(e)}'}, status=404)
    
    @csrf_exempt
    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)
    
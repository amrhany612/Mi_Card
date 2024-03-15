from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status,viewsets


# Create your views here.


class HelloApiView(APIView):

    def get(self,request,format=None):

        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'it is similar to traditional  django view',
            'Gives you the most control over tour logic',
            'it is mapped manually to urls'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):

        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):

        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):

        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
   
    
    serializer_class = serializers.HelloSerializer


    def list(self,request):
        a_viewset = [
            'uses actions (list,create,update,partial update)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset}) 
    
    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,requet,pk=None):

        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):

        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):

            return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):

        return Response({'http_method':'DELETE'})
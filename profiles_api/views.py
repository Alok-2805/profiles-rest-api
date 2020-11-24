from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    '''Test API View'''
    def get(self,request,format=None):
        '''Returns a list of APIView features'''
        an_apiview=['uses http methods as function (get,post,patch,put,delete)','is similar to django api','gives u the most control over ypur applocation logic','is mapped manually to urls',]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        '''create a hello message with our name'''
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''Handle a partial update of an object'''
        return Response({'method':'Patch'})

    def delete(self,rquest,pk=None):
        ''' Handle deleting of an Object'''
        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    '''Test API Viewsets'''
    serializer_class=serializers.HelloSerializer

    def list(self,reuest):
        a_viewset=[ 'Uses actions [list,crete,retrieve,update,partial_update]',
        'Automatically maps to URLs using Routers','Provides more functionality with less code']
        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self,request):
        '''Create  a new hello message'''
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        '''Handle getting an object by its ID'''
        return Response({'http_method':'Get'})

    def update(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'http_method':'Put'})

    def partial_update(self,request,pk=None):
        '''Handle updating part of  an object '''
        return Response({'http_method':'Patch'})

    def destroy(self,request,pk=None):
        '''Handle removing an object '''
        return Response({'http_method':'Delete'})



class UserProfilesViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

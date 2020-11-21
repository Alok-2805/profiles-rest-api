from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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

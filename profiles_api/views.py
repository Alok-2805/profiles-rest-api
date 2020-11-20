from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View'''
    def get(self,request,format=None):
        '''Returns a list of APIView features'''
        an_apiview=['uses http methods as function (get,post,patch,put,delete)','is similar to django api','gives u the most control over ypur applocation logic','is mapped manually to urls',]
        return Response({'message':'Hello!','an_apiview':an_apiview})

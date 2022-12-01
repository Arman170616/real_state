from django.shortcuts import render

from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.response import Response

from rest_framework.views import APIView
from realtor.models import Agent
from realtor.serializers import AgentSerializer

class Search(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data 
        str = data['str']
        q = (Q(name_icontains=str)) | (Q(biodata_icontains=str))
        queryset = Agent.objects.filter(q)
        serializer = AgentSerializer(queryset, many= True)
        return Response(serializer.data)

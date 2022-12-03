from django.shortcuts import render

from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Home, ImageFiles
from .serializers import HomeSerializer, HomeDetailSerializer, ImageFilesSerializer

class HomeListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'

class HomeDetailAPIView(RetrieveAPIView):
    serializer_class = HomeDetailSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class ImageView(APIView):

    def get(self, request, pk, format=None):
        home = Home.objects.get(pk=pk)
        images = home.images.all()
        serializer = ImageFilesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# class Search(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request, format=None):
#         data = self.request.data 
#         str = data['str']
#         q = (Q(name_icontains=str)) | (Q(biodata_icontains=str))
#         queryset = Agent.objects.filter(q)
#         serializer = AgentSerializer(queryset, many= True)
#         return Response(serializer.data)

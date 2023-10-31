from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CarsSerializer


class CarsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page-size'
    max_page_size = 100


class CarsAPIList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CarsAPIListPagination


class CarsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class CarsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class CarsViewSet(viewsets.ModelViewSet):
#     #queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Cars.objects.all()[:3]
#
#         return Cars.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

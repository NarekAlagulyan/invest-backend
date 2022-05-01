from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.viewsets import ViewSet
from rest_framework.serializers import ModelSerializer

from helpers.response import Response
from helpers.shortcuts import get_object_or_404


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UserViewSet(ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
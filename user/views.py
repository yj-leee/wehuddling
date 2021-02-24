import jwt
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


from drf_yasg.utils import swagger_auto_schema


from .models import User
from .serializers import UserSerializer, UserLoginSerializer

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']
            serializer.validated_data['password'] = make_password(password)
            user = serializer.save()

            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(generics.GenericAPIView):
    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validte(raise_exception=True)
            response = {
                "success" : "True",
                "status_code" : status.HTTP_200_OK,
                "message" : "Login Success",
                "token" : serializer.data['token']
            }
            stauts_code = status.HTTP_200_OK

        return Response(response, status=status_code)


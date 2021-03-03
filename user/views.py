from django.shortcuts                import get_object_or_404, render
from django.contrib.auth             import authenticate
from django.contrib.auth.hashers     import check_password, make_password

from rest_framework                  import status
from rest_framework.views            import APIView
from rest_framework.response         import Response
from rest_framework.authtoken.models import Token

from drf_yasg.utils                  import swagger_auto_schema

from .models                         import User
from .serializers                    import UserSerializer, UserLoginSerializer

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']
            serializer.validated_data['password'] = make_password(password)
            user     = serializer.save()
            token    = Token.objects.create(user=user)

            if user:
                return Response({"token":token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email    = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user     = authenticate(email=email, password=password)

            if user:
                token = Token.objects.get(user=user)
                return Response({"Token":token.key})
        return Response(status=401)


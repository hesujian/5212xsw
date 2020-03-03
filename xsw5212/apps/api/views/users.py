
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

from api import serializers
from utils.response import APIResponse
from api import models


class RegisterAPIView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        ser = serializers.RegisterSerializer(data=data)
        if ser.is_valid():
            user_obj = models.User.objects.create_user(**ser.data)
            return APIResponse(200, 'ok')
        else:
            print(ser.errors)
        return APIResponse(300, ser.errors)


class LoginAPIView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = auth.authenticate(request=request, username=username, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            token = 'jwt ' + token
            return APIResponse(200, 'ok', data_res={
                'token': token,
                'username': user.username
            })
        else:
            return APIResponse(300, '账号或密码错误')

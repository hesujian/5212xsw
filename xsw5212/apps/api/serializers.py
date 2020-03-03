import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'tel', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'username': {
                'error_messages': {
                    'required': '用户名不能为空',
                }
            },
            'password': {
                'error_messages': {
                    'required': '密码不能为空',
                }

            },
            'confirm_password': {
                'error_messages': {
                    'required': '重复密码不能为空',
                }

            }
        }

    def validate_tel(self, value):
        if re.match(r'^1[3-9]\d{9}$', str(value)):
            return value
        else:
            raise ValidationError('手机号格式不正确')

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password == password:
            return attrs
        else:
            raise ValidationError({'password': '两次密码输入不一致'})
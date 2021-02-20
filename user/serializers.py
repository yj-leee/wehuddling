from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


#class UserSerializer(serializers.Serializer):
#    class Meta:
#        id = serializers.IntegerField(read_only=True)
#        email = serializers.EmailField()
#        password = serializers.CharField()
#        name = serializers.CharField()
#        phone_number = serializers.CharField()
#        gender = serializers.CharField()
#        address = serializers.CharField()
#        is_deleted = serializers.BooleanField()
#        create_at = serializers.DateTimeField(read_only=True)
#        update_at = serializers.DateTimeField(read_only=True)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)
    name = serializers.CharField()
    phone_number = serializers.CharField()
    gender = serializers.CharField(required=False,allow_blank=True)
    address = serializers.CharField(required=False,allow_blank=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone_number', 'gender', 'address')








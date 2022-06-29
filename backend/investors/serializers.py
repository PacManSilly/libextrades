from dj_rest_auth import serializers as dj_rest_auth_serializer
from .models import InvestorInvestment, InvestorWithdrawal
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'username', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.other_name = validated_data.get('other_name', instance.other_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.mugshot = validated_data.get('mugshot', instance.mugshot)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.postal = validated_data.get('postal', instance.postal)
        instance.kyc_front_view = validated_data.get('kyc_front_view', instance.kyc_front_view)
        instance.kyc_back_view = validated_data.get('kyc_back_view', instance.kyc_back_view)
        instance.save()

        return instance


class InvestorInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInvestment
        fields = "__all__"


class InvestorWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorWithdrawal
        fields = "__all__"


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def to_internal_value(self, data):
        if data.get('email'):
            data['email'] = data['email'].lower()

        return super().to_internal_value(data)

class CustomDjRestAuthLoginSerializer(dj_rest_auth_serializer.LoginSerializer):
    """"
    Custom dj_rest_auth Login_serializer class, subclassing the default LoginSerializer from dj_rest_auth
    to get rid of the email field, because the username field can server both purposes.
    """
    username = serializers.CharField()
    password = serializers.CharField()
    email = None


class CustomDjRestAuthJWTSerializer(dj_rest_auth_serializer.JWTSerializer):
    """
    Custom dj_rest_auth jwt_serializer class subclassing the default JWTSerializer to get rid of the user
    instance data returned.
    """
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = None

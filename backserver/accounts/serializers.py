from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
# from django.contrib.auth import get_user_model



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    # email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    sex = serializers.CharField(max_length=10)
    earn = serializers.IntegerField()

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if allauth_account_settings.UNIQUE_EMAIL:
    #         if email and email_address_exists(email):
    #             raise serializers.ValidationError(
    #                 _('A user is already registered with this e-mail address.'),
    #             )
    #     return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def validate_nickname(self, nickname):
        # nickname 필드의 유효성 검사 메서드
        # 닉네임은 필수 요소
        if not nickname:
            raise serializers.ValidationError("Nickname is required.")
        # 닉네임은 최대 50자로 제한하고 특수 문자를 허용하지 않음
        if len(nickname) > 100:
            raise serializers.ValidationError("Nickname must be at most 100 characters.")
        if not nickname.isalnum():
            raise serializers.ValidationError("Nickname can only contain alphanumeric characters.")
        return nickname

    def validate_age(self, age):
        # age 필드의 유효성 검사 메서드
        # 나이는 양수여야 함
        if age is not None and age <= 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return age

    def validate_sex(self, sex):
        # sex 필드의 유효성 검사 메서드
        # 성별은 'male' 또는 'female'만 허용
        if sex not in ['male', 'female']:
            raise serializers.ValidationError("Invalid sex. Allowed values are 'male' and 'female'.")
        return sex

    def validate_earn(self, earn):
        if earn is not None and earn < 0:
            raise serializers.ValidationError("Earn must be a non-negative number.")
        return earn

    def custom_signup(self, request, user):
        pass



    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            # 'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'sex': self.validated_data.get('sex', ''),
            'earn': self.validated_data.get('earn', ''),
        }

    def save(self, request):
        # allauth 의 기본 adaper 를 가져옴
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        # 기본 adaper 의 save_user 는 nickname 필드를
        # 저장하지 않는다!
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'age', 'sex', 'earn', 'is_superuser', 'my_deposit', 'my_saving']
        fields = '__all__'


class UserDepositProducts(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['my_deposit', ]


class UserSavingProducts(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['my_saving', ]

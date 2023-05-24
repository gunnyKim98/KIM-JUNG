from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter


class User(AbstractUser):
    # 기본적으로 제공되는 필드
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20, default='Gil-Dong', null=True)
    last_name = models.CharField(max_length=20, default='Hong', null=True)
    # email = models.EmailField(max_length=100)
    # 추가적인 사용자 정의 필드
    nickname = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    sex = models.CharField(default='female', max_length=10, blank=True, null=True)
    earn = models.IntegerField(default=1000, blank=True, null=True)
    my_deposit = models.JSONField(default=list, blank=True, null=True)
    my_saving = models.JSONField(default=list, blank=True, null=True)


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        # email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        sex = data.get("sex")
        earn = data.get("earn")

        # user_email(user, email)
        user_username(user, username)

        # if age:
        #     user_field(user, "age", age)
        # if sex:
        #     user_field(user, "sex", sex)
        # if earn:
        #     user_field(user, "earn", earn)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user_field(user, "age", str(age))
        if sex:
            user_field(user, "sex", str(sex))
        if earn:
            user_field(user, "earn", str(earn))

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user

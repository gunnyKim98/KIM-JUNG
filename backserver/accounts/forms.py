from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = get_user_model()
#         fields = ('username', 'email', 'first_name', 'last_name', 'nickname', 'age', 'sex', 'earn')
#

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'age', 'earn')

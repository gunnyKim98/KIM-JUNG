from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import CustomUserChangeForm
from .models import User


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'detail': 'Invalid credentials'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def update_user(request):
#     print(request.data)
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         print(form)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             serializer = UserSerializer(user)
#             print(serializer)
#             return Response(serializer.data)
#         return Response({'errors': form.errors}, status=400)
#     form = CustomUserChangeForm(instance=request.user)
#     form_data = {field: form[field].value() for field in form.fields}
#     context = {
#         'form': form_data
#     }
#     print(context)
#     return Response(context)
def update_user(request):
    data = request.data
    print(data)

    if request.method == 'POST':
        form = CustomUserChangeForm(data, instance=request.user)
        print(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            serializer = UserSerializer(user)
            print(serializer)
            return Response(serializer.data)
        return Response({'errors': form.errors}, status=400)

    form = CustomUserChangeForm(instance=request.user)
    form_data = {field: form[field].value() for field in form.fields}
    context = {
        'form': form_data
    }
    print(context)
    return Response(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_my_saving(request, user_pk):
    if request.method == 'POST':
        data = request.data
        print(data)
        user = User.objects.get(id=user_pk)
        print(user)
        my_saving = user.my_saving or []
        my_saving.append(dict(data))
        user.my_saving = my_saving
        user.save()
        return Response({'message': 'Data added to my_saving successfully.'})
    return Response({'error': 'Invalid request method.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_my_deposit(request, user_pk):
    if request.method == 'POST':
        data = request.data
        print(data)
        user = User.objects.get(id=user_pk)
        print(user)
        my_deposit = user.my_deposit or []
        my_deposit.append(dict(data))
        user.my_deposit = my_deposit
        user.save()
        return Response({'message': 'Data added to my_deposit successfully.'})
    return Response({'error': 'Invalid request method.'})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .serializers import UserSerializer, UserDepositProducts, UserSavingProducts
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import CustomUserChangeForm
from .models import User
from django.db.models import Count
from collections import defaultdict


@api_view(['GET'])
def viewDepositProductAge(request, user_pk):
    now_login = User.objects.get(id=user_pk)
    users = User.objects.all()
    serializer = UserDepositProducts(users, many=True)
    output = [item.get("my_deposit", []) for item in serializer.data if len(item.get("my_deposit", [])) > 0]
    product_stats = defaultdict(lambda: {'age_sum': 0, 'earn_sum': 0, 'count': 0})

    for i in output:
        for j in range(len(i)):
            product_name = i[j]['title']
            age = i[j]['age']
            earn = i[j]['earn']

            product_stats[product_name]['age_sum'] += age
            product_stats[product_name]['earn_sum'] += earn
            product_stats[product_name]['count'] += 1

    res = [{'상품명': product_name, '나이차': abs(stats['age_sum'] / stats['count'] - now_login.age), '소득차': abs(stats['earn_sum'] / stats['count'] - now_login.earn)}
           for product_name, stats in product_stats.items()]
    sorted_res = sorted(res, key=lambda x: x['나이차'])
    return Response(sorted_res)


@api_view(['GET'])
def viewDepositProductEarn(request, user_pk):
    now_login = User.objects.get(id=user_pk)
    users = User.objects.all()
    serializer = UserDepositProducts(users, many=True)
    output = [item.get("my_deposit", []) for item in serializer.data if len(item.get("my_deposit", [])) > 0]
    product_stats = defaultdict(lambda: {'age_sum': 0, 'earn_sum': 0, 'count': 0})

    for i in output:
        for j in range(len(i)):
            product_name = i[j]['title']
            age = i[j]['age']
            earn = i[j]['earn']

            product_stats[product_name]['age_sum'] += age
            product_stats[product_name]['earn_sum'] += earn
            product_stats[product_name]['count'] += 1


    res = [{'상품명': product_name, '나이차': abs(stats['age_sum'] / stats['count'] - now_login.age), '소득차': abs(stats['earn_sum'] / stats['count'] - now_login.earn)}
           for product_name, stats in product_stats.items()]
    sorted_res = sorted(res, key=lambda x: x['소득차'])
    return Response(sorted_res)

# @api_view(['GET'])
# def viewSavingProduct1(request):
#     users = User.objects.all()
#     serializer = UserSavingProducts(users, many=True)
#     # output = [item for item in serializer.data if len(item.get("my_saving", [])) > 0]
#     output = [item.get("my_saving", []) for item in serializer.data if len(item.get("my_saving", [])) > 0]
#     res = []
#     for i in output:
#         for j in range(len(i)):
#             res.append({'상품명': i[j]['title'], '나이': i[j]['age'], '소득': i[j]['earn']})
#     print(len(res))
#     sorted_res = sorted(res, key=lambda x: x['상품명'])
#     return Response(sorted_res)

@api_view(['GET'])
def viewSavingProductAge(request, user_pk):
    now_login = User.objects.get(id=user_pk)
    users = User.objects.all()
    serializer = UserSavingProducts(users, many=True)
    # output = [item for item in serializer.data if len(item.get("my_saving", [])) > 0]
    output = [item.get("my_saving", []) for item in serializer.data if len(item.get("my_saving", [])) > 0]
    product_stats = defaultdict(lambda: {'age_sum': 0, 'earn_sum': 0, 'count': 0})

    for i in output:
        for j in range(len(i)):
            product_name = i[j]['title']
            age = i[j]['age']
            earn = i[j]['earn']

            product_stats[product_name]['age_sum'] += age
            product_stats[product_name]['earn_sum'] += earn
            product_stats[product_name]['count'] += 1

    res = [{'상품명': product_name, '나이차': abs(stats['age_sum'] / stats['count'] - now_login.age), '소득차': abs(stats['earn_sum'] / stats['count'] - now_login.earn)}
           for product_name, stats in product_stats.items()]
    sorted_res = sorted(res, key=lambda x: x['나이차'])
    return Response(sorted_res)


@api_view(['GET'])
def viewSavingProductEarn(request, user_pk):
    now_login = User.objects.get(id=user_pk)
    users = User.objects.all()
    serializer = UserSavingProducts(users, many=True)
    # output = [item for item in serializer.data if len(item.get("my_saving", [])) > 0]
    output = [item.get("my_saving", []) for item in serializer.data if len(item.get("my_saving", [])) > 0]
    product_stats = defaultdict(lambda: {'age_sum': 0, 'earn_sum': 0, 'count': 0})

    for i in output:
        for j in range(len(i)):
            product_name = i[j]['title']
            age = i[j]['age']
            earn = i[j]['earn']

            product_stats[product_name]['age_sum'] += age
            product_stats[product_name]['earn_sum'] += earn
            product_stats[product_name]['count'] += 1

    res = [{'상품명': product_name, '나이차': abs(stats['age_sum'] / stats['count'] - now_login.age), '소득차': abs(stats['earn_sum'] / stats['count'] - now_login.earn)}
           for product_name, stats in product_stats.items()]
    sorted_res = sorted(res, key=lambda x: x['소득차'])
    return Response(sorted_res)

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
@permission_classes([IsAuthenticated])
def update_user(request):
    data = request.data
    if request.method == 'POST':
        form = CustomUserChangeForm(data, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            serializer = UserSerializer(user)
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
        user = User.objects.get(id=user_pk)
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
        user = User.objects.get(id=user_pk)
        my_deposit = user.my_deposit or []
        my_deposit.append(dict(data))
        user.my_deposit = my_deposit
        user.save()
        return Response({'message': 'Data added to my_deposit successfully.'})
    return Response({'error': 'Invalid request method.'})

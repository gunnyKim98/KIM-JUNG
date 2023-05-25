import requests
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingOptionsSerializer, SavingProductsSerializer
from django.db.models import Max
from datetime import datetime
import requests

BASE_URL = 'https://finlife.fss.or.kr/finlifeapi/'
API_KEY1 = settings.API_KEY1
API_KEY2 = settings.API_KEY2

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': API_KEY1,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    res = response['result']['baseList']
    ols = response['result']['optionList']
    # return JsonResponse({'res': res})
    for info in res:
        serializer1 = DepositProductsSerializer(data=info)
        if serializer1.is_valid():
            serializer1.save()

    for ol in ols:
        idx = DepositProducts.objects.get(fin_prdt_cd=ol['fin_prdt_cd'])
        for key in ol.keys():
            if ol[key] is None:
                ol[key] = '-'
        serializer2 = DepositOptionsSerializer(data=ol)

        if serializer2.is_valid():
            serializer2.save(fin_prdt_cd=idx)
    return Response(res)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def deposit_product_options(request):
    products = DepositOptions.objects.all()
    serializer = DepositOptionsSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': API_KEY1,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    res = response['result']['baseList']
    ols = response['result']['optionList']

    for info in res:
        serializer3 = SavingProductsSerializer(data=info)
        if serializer3.is_valid():
            saving_product = serializer3.save()
            if saving_product:
                saving_product.save()

    for ol in ols:
        idx = SavingProducts.objects.get(fin_prdt_cd=ol['fin_prdt_cd'])
        for key in ol.keys():
            if ol[key] is None:
                ol[key] = '-'
        serializer2 = SavingOptionsSerializer(data=ol)

        if serializer2.is_valid():
            serializer2.save(fin_prdt_cd=idx)  # SavingOptions 객체 저장

    return Response(response['result']['baseList'])

@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == "GET":
        products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def saving_product_options(request):
    products = SavingOptions.objects.all()
    serializer = SavingOptionsSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def exchange_money(request):
    now = datetime.now()
    a = str(now.year)
    if now.month < 10:
        b = str(0) + str(now.month)
    else:
        b = str(now.month)
    c = str(now.day)
    ans = str(a+b+c)
    KEY = API_KEY2
    URL = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={KEY}&searchdate={ans}&data=AP01"
    response = requests.get(URL)
    response.raise_for_status()  # 요청이 성공적이지 않은 경우 예외 발생
    datas = response.json()  # JSON 데이터를 파싱하여 Python 객체로 변환
    res = []

    for i in range(len(datas)):
        try:
            country, currency = datas[i]['cur_nm'].split()
        except:
            currency = datas[i]['cur_nm']
            if currency == '위안화':
                country = '중국'
            else:
                country = '유럽'

        if country == '일본' or country == '인도네시아':
            rate = str(round(float(datas[i]['deal_bas_r'].replace(',',''))/100,3))
        else:
            rate = datas[i]['deal_bas_r'].replace(',','')

        context = {
            'country': country,
            'currency': currency,
            'rate': rate
        }
        res.append(context)

    return Response(res)


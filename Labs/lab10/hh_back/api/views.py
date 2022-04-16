from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt

#FBV
@csrf_exempt
@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanyMSerializer(companies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanyMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def each_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'message' : str(e)}, status=400)
    if request.method == 'GET':
        serializer = CompanyMSerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanyMSerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return Response({'message': 'deleted'}, status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VacancySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def each_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'message' : str(e)}, status=400)
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'message': 'deleted'}, status=204)

@csrf_exempt
@api_view(['GET'])
def vacancy_by_company(request, company_id): 
    try:
        vacancies = Vacancy.objects.filter(company=company_id)
    except len(vacancies) == 0:
        return Response({'message' : 'No such element'}, status=400)
    if request.method == 'GET':
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def ten_vacancy(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

#CBV
class CompanyAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyMSerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        serializer = CompanyMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
    @csrf_exempt
    def get_object(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def get(self, request, company_id=None):
        company = self.get_object(company_id)
        serializer = CompanyMSerializer(company)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    @csrf_exempt
    def put(self, request, company_id=None):
        company = self.get_object(company_id)
        serializer = CompanyMSerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, company_id=None):
        company = self.get_object(company_id)
        company.delete()
        return Response({'message': 'deleted'},  status=status.HTTP_200_OK)
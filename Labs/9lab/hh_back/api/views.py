from django.http import JsonResponse
from api.models import Company, Vacancy
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.makeJson() for company in companies]
        return JsonResponse(companies_json, safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        new_company = Company.objects.create(
            name=data['name'],
            description=data['description'],
            city=data['city'],
            address=data['address'] 
        )
        return JsonResponse(new_company.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)

@csrf_exempt
def each_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message' : str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(company.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if 'name' in data.keys():
            company.name = data['name']
        if 'description' in data.keys():
            company.description = data['description']
        if 'city' in data.keys():
            company.city = data['city']
        if 'address' in data.keys():
            company.address = data['address']
        company.save()
        return JsonResponse(company.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message':'OK'}, safe=False, json_dumps_params={'indent' : 4}, status=200)

@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancy = Vacancy.objects.create(
            name=data['name'],
            description=data['description'],
            salary=data['salary'],
            company=Company.objects.get(id=int(data['company']))
        )
        return JsonResponse(vacancy.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)
    
@csrf_exempt
def each_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message' : str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(vacancy.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if 'name' in data.keys():
            vacancy.name = data['name']
        if 'description' in data.keys():
            vacancy.description = data['description']
        if 'salary' in data.keys():
            vacancy.salary = data['salary']
        vacancy.save()
        return JsonResponse(vacancy.makeJson(), safe=False, json_dumps_params={'indent' : 4}, status=200)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'OK'}, safe=False, json_dumps_params={'indent' : 4}, status=200)

@csrf_exempt
def vacancy_by_company(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company=company_id)
    except len(vacancies) == 0:
        return JsonResponse({'message' : 'No such element'}, status=400)
    if request.method == 'GET':
        vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4}, status=200)

@csrf_exempt
def ten_vacancy(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4}, status=200)

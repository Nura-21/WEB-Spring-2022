from django.http import JsonResponse
from api.models import Company, Vacancy

# Create your views here.
def companies(request):
    companies = Company.objects.all()
    companies_json = [company.makeJson() for company in companies]
    return JsonResponse(companies_json, safe=False, json_dumps_params={'indent' : 4})

def each_company(requst, company_id):
    company = Company.objects.get(id=company_id)
    return JsonResponse(company.makeJson(), safe=False, json_dumps_params={'indent' : 4})

def vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4})

def each_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    return JsonResponse(vacancy.makeJson(), safe=False, json_dumps_params={'indent' : 4})


def vacancy_by_company(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4})

def ten_vacancy(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.makeJson() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False, json_dumps_params={'indent' : 4})

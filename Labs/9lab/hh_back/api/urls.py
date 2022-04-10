from django.urls import path
from api.views import companies, each_company, vacancies, each_vacancy, vacancy_by_company, ten_vacancy

urlpatterns = [
    path('companies/', companies),
    path('companies/<int:company_id>/', each_company),
    path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', each_vacancy),
    path('vacancies/top_ten/', ten_vacancy),
]
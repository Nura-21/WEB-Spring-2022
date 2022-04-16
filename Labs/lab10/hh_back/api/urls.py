from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import * 
urlpatterns = [
    path('companies/', companies),
    path('companies/<int:company_id>/', each_company),
    path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', each_vacancy),
    path('vacancies/top_ten/', ten_vacancy),
    path('login/', obtain_jwt_token),
]
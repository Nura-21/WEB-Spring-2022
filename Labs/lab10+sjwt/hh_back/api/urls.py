from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('companies/', companies),
    path('companies/<int:company_id>/', each_company),
    path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', each_vacancy),
    path('vacancies/top_ten/', ten_vacancy),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
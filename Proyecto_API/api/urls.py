from django.urls import path
from .views import companyView

urlpatterns = [
    path('companies/',companyView.as_view(), name='companies_list'),
    path('companies/<int:id>',companyView.as_view(), name='companies_process')
]

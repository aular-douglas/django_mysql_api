from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json 

# Create your views here.

class companyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self ,request,id=0):
        if (id>0):
            companies=list(company.objects.filter(id=id).values())
            if len(companies)> 0:
                company = companies[0]
                datos = {'message': "success", 'company': company}
            else:
                return JsonResponse(datos)
                
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos={'message':"Success",'companies':companies}
            else:
                datos={'message':"companies not found..."}
            return JsonResponse(datos)
    
    def post(self ,request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
 
    def putt(self ,request,id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'massage': "success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self ,request,id):
        companies = list(company.objects.filter(id=id).values())
        if len(companies) > 0:
            company.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message':"Company not found..."}
        return JsonResponse(datos)    

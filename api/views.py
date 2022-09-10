from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views import View
from .models import Company
import json

# Create your views here.

class CompanyView(View):
    def get(self, request, id = 0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
                 
            if len(companies) > 0:
                company = companies[0]
                data = {'message': 'Success', 'company': company}
            else:
                data = {'message': 'Company not found'}
            return JsonResponse(data)

        else:
            companies = list(Company.objects.values())

            if len(companies) > 0:
              data = {'message': 'Success', 'companies': companies}
            else:
              data = {'message': 'Companies not found ...'}
            return JsonResponse(data)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        json_data = json.loads(request.body)

        Company.objects.create(
            name=json_data['name'],
            address=json_data['address'],
            city=json_data['city'],
            country=json_data['country'],
        )

        data = {'message': 'Company created successfully'}
        return JsonResponse(data)

    def put(self, request, id):
        json_data = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())

        if len(companies) > 0:
            company = Company.objects.get(id=id)

            company.name = json_data['name']
            company.address = json_data['address']
            company.city = json_data['city']
            company.country = json_data['country']
            company.save()

            data = {'message': 'Company updated successfully'}

        else:
            data = {'message': 'Company not found'}
        return JsonResponse(data)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())

        if len(companies) > 0:
            Company.objects.get(id=id).delete()

            data = {'message': 'Company deleted successfully'}

        else:
            data = {'message': 'Company not found'}
        return JsonResponse(data)

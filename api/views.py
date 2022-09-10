from django.http.response import JsonResponse
from django.views import View
from .models import Company

# Create your views here.

class CompanyView(View):
    def get(self, request):
        companies = list(Company.objects.values())

        if len(companies) > 0:
            data = {'message': 'Success', 'companies': companies}
        else:
            data = {'message': 'Companies not found ...'}
        return JsonResponse(data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

from budgets.models import Budget
from budgets.serializers import BudgetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class BudgetList(APIView):
    """
    List all the budgets.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Budget.objects.all()
        return Response({'budgets', queryset})

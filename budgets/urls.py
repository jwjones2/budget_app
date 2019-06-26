from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from budgets import views

urlpatterns = [
    path('home/', views.BudgetList.as_view()),
    path('budgets/', views.BudgetList.as_view()),
    path('budget/', views.BudgetCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
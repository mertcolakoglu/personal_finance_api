from django.urls import path
from . import views

urlpatterns = [
    path('budgets/', views.BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', views.BudgetRetrieveUpdateDestroyView.as_view(), name='budget-retrieve-update-destroy'),
]
from django.urls import path
from .views import TransactionListCreateView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
]
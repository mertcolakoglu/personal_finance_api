from django.urls import path
from .views import AccountListViews, AccountDetailView, AccountBalanceView

urlpatterns = [
    path('accounts/', AccountListViews.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/<int:pk>/balance/', AccountBalanceView.as_view(), name='account-balance'),
]
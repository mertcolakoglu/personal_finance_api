from django.urls import path
from .views import GoalListCreateAPIView, GoalDetailView

urlpatterns = [
    path('goals/', GoalListCreateAPIView.as_view(), name='goal-list'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
]
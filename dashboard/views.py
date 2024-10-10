from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from accounts.models import Account
from transactions.models import Transaction
from budgets.models import Budget
from goals.models import Goal

# Create your views here.

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()
        month_start = today.replace(day=1)
        month_end = (month_start + relativedelta(months=1)) - relativedelta(days=1)

        accounts = Account.objects.filter(user=user)
        total_balance = accounts.aggregate(Sum('balance'))['balance__sum'] or 0

        income = Transaction.objects.filter(
            user=user, 
            transaction_type='income', 
            date__range=[month_start, month_end]
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        expenses = Transaction.objects.filter(
            user=user, 
            transaction_type='expense', 
            date__range=[month_start, month_end]
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        budgets = Budget.objects.filter(user=user, start_date__lte=today, period='monthly')
        budget_status = []
        for budget in budgets:
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                transaction_type='expense',
                date__range=[month_start, month_end]
            ).aggregate(Sum('amount'))['amount__sum'] or 0
            budget_status.append({
                'category': budget.category.name,
                'budget_amount': budget.amount,
                'spent': abs(spent),
                'remaining': budget.amount - abs(spent)
            })

        goals = Goal.objects.filter(user=user, status='in_progress')
        goal_status = [{
            'name': goal.name,
            'target_amount': goal.target_amount,
            'current_amount': goal.current_amount,
            'progress_percentage': goal.progress_percentage,
            'days_left': (goal.deadline - today).days
        } for goal in goals]

        return Response({
            'total_balance': total_balance,
            'monthly_income': income,
            'monthly_expenses': abs(expenses),
            'budget_status': budget_status,
            'goal_status': goal_status
        })
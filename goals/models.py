from django.db import models
from django.conf import settings

# Create your models here.

class Goal(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('achieved', 'Achieved'),
        ('abandoned', 'Abandoned'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.current_amount}/{self.target_amount}"

    @property
    def progress_percentage(self):
        return (self.current_amount / self.target_amount) * 100 if self.target_amount > 0 else 0
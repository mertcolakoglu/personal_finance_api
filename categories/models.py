from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    CATEGORY_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=50, choices=CATEGORY_TYPE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('name', 'user')

    def __str__(self):
        return f"{self.name} ({self.ge_category_type_display()})"
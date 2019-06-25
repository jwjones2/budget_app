from django.db import models

class Budget(models.Model):
    budget_types = [
        ('house', 'household'),
        ('proj', 'project'),
        ('save', 'saving'),
        ('sp', 'special'),
    ]

    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    amount      = models.CharField(max_length=50, blank=True)
    end_date    = models.DateTimeField()
    purpose     = models.CharField(choices=budget_types, max_length=50, default='household')


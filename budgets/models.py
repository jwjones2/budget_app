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
    end_date    = models.DateTimeField()
    purpose     = models.CharField(choices=budget_types, max_length=50, default='household')

class Item(models.Model):
    """
    Items are actual things, areas, expenses, etc. that are budgeted for.
    For instance, car insurance, house payment, savings, and so on.
    Amount here specifies the budgeted amount for this item.
    Tied to a budget.
    """
    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    amount      = models.CharField(max_length=50, blank=True)
    budget      = models.ForeignKey(Budget, on_delete=models.CASCADE)

class Category(models.Model):
    """
    Categories are a grouping of items.  This allows for logical
    grouping within a budget.  
    Tied to a budget.
    """
    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    budget      = models.ForeignKey(Budget, on_delete=models.CASCADE)

class Income(models.Model):
    """
    Income sources for a budget.  Amount refers to the income amount.
    Tied to a budget.
    """
    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    amount      = models.CharField(max_length=50, blank=True)
    budget      = models.ForeignKey(Budget, on_delete=models.CASCADE)

class Entry(models.Model):
    """
    This is a credit or debit logged for a budget.
    These are the actual monthly (or other time period) expenditures or returns, etc.
    Receipt is a link to an uploaded file to store images of reciepts.
    Tied to a category.
    """
    entry_types = [
        ('C', 'credit'),
        ('D', 'debit'),
    ]

    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    amount      = models.CharField(max_length=50, blank=True)
    type        = models.CharField(choices=entry_types, max_length=50, default='debit')
    receipt     = models.CharField(max_length=200, blank=True)
    category    = models.ForeignKey(Budget, on_delete=models.CASCADE)



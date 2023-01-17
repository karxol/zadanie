from django.contrib import admin
from .models import Expense

# Register your models here.

#admin.site.register(Expense)

@admin.register(Expense)

class tasks(admin.ModelAdmin):
    list_filter = ["date"]

from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'dateOfBirth', 'hobby', 'avatar', 'coverPhoto']
    list_filter = ['user']
    search_fields = ['user']
admin.site.register(Account, AccountAdmin)
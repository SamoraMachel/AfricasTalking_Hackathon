from django.contrib import admin

# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import USSD, UserReg


@admin.register(USSD)
class USSDAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sessionId',
        'phoneNumber',
        'networkCode',
        'serviceCode',
        'text',
    )


@admin.register(UserReg)
class UserRegAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'location')
    search_fields = ('name',)
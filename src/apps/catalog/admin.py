from django.contrib import admin
from catalog import models


class PasswordRecoveryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'status', 'sending_status')


class EmailValidationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'status', 'sending_status')


admin.site.register(models.City)
admin.site.register(models.Category)
admin.site.register(models.PasswordRecovery, PasswordRecoveryAdmin)
admin.site.register(models.EmailValidation, EmailValidationAdmin)

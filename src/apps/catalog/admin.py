from django.contrib import admin
from catalog.models import category, city, token, statistics


class PasswordRecoveryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'status', 'sending_status')


class EmailValidationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'status', 'sending_status')


admin.site.register(city.City)
admin.site.register(category.Category)
admin.site.register(token.PasswordRecovery, PasswordRecoveryAdmin)
admin.site.register(token.EmailValidation, EmailValidationAdmin)
admin.site.register(statistics.CategoryStatistics)
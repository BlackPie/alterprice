from django.contrib import admin
from apuser import models


admin.site.register(models.AlterPriceUser)
admin.site.register(models.ClientProfile)
admin.site.register(models.OperatorProfile)
admin.site.register(models.AdminProfile)

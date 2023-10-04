from django.contrib import admin
from .models import Bulb,ALL_ISSUES_MODELS

admin.site.register(Bulb)
for model in ALL_ISSUES_MODELS :
    admin.site.register(model)
# Register your models here.

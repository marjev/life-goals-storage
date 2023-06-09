from django.contrib import admin

from .models import ComputerScienceEducatorsPost, CseEndeavour


admin.register(ComputerScienceEducatorsPost, CseEndeavour)(admin.ModelAdmin)

from django.contrib import admin
from .models import Caterogy


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.register(Caterogy, CategoryAdmin)

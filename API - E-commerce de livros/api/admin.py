from django.contrib import admin

from api.models import Livros


@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    exclude = ()


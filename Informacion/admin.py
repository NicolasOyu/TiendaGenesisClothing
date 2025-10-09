from django.contrib import admin
from .models import Categoria, Post

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("titulo","slug","created")
    search_fields = ("titulo",)
    prepopulated_fields = {"slug": ("titulo",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo","autor","publicado","created")
    list_filter = ("publicado","categorias")
    search_fields = ("titulo","contenido","autor__username")
    filter_horizontal = ("categorias",)
    readonly_fields = ("created","updated")
    prepopulated_fields = {"slug": ("titulo",)}
    def save_model(self, request, obj, form, change):
        if obj.autor is None:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


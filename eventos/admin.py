from django.contrib import admin
from eventos.models import Evento, Local, Categoria, Atividade, Relatorio, Inscricao
# Register your models here.

class AtividadeInLine(admin.TabularInline):
    model = Atividade
    extra = 1
class RelatorioInLine(admin.TabularInline):
    model = Relatorio
    extra = 1
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'inicio', 'local']
    list_filter = ['local', 'categoria']
    search_fields = ['titulo']
    in_lines = [AtividadeInLine,RelatorioInLine]

admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Atividade)
admin.site.register(Relatorio)
admin.site.register(Inscricao)
from django.contrib import admin

# Register your models here.

from .models import Fachekehu, Daozhan, Baozhuang, Guige, Huowu, Fache, Jisuan


class JisuanInline(admin.TabularInline):
    model = Jisuan


@admin.register(Fache)
class FacheAdmin(admin.ModelAdmin):
    list_display = ['date', 'daozhan', 'huowu', 'fachekehu']
    inlines = [JisuanInline]


admin.site.register(Fachekehu)
admin.site.register(Daozhan)
admin.site.register(Baozhuang)
admin.site.register(Guige)
admin.site.register(Huowu)
# admin.site.register(Fache)
# admin.site.register(Jisuan)



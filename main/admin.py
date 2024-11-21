from django.contrib import admin
from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'guruh', 'kurs', 'kitob_soni')
    list_display_links = ('ism', 'guruh')
    list_editable = ('kurs', 'kitob_soni')
    list_filter = ('kurs',)
    search_fields = ('ism', 'guruh')


class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'olingan_sana'


# StackedInline - ustma-ust
# TabularInline - yonma-yon

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism', 'jins', 'tugilgan_sana', 'kitob_soni', 'tirik',)
    inlines = (KitobInline,)


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi)
admin.site.register(Record, RecordAdmin)

from django.contrib.auth.models import Group, User

admin.site.unregister([Group, User])

from django.contrib import admin
from .models import Magazine
from .models import Static_Texts


class MagazineAdmin(admin.ModelAdmin):
    list_display =('id','name','created_date','isPublished')
    list_display_links =('id','name')
    list_filter=('created_date',)
    list_editable=('isPublished',)
    search_fields =('name','description')
    list_per_page=10

class Static_Texts_Admin(admin.ModelAdmin):
    list_display =('id','name',)
    list_display_links =('id','name')
    list_filter=('created_date','name')
    search_fields =('name',)
    list_per_page=10



# Register your models here.

admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Static_Texts, Static_Texts_Admin)

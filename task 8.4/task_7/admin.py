from django.contrib import admin
from .models import Advertisement

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description","price","auction","created_date","updated_date"]
    list_filter = ["auction", "created_at"]
    actions = ["set_auction_false","set_auction_true"]

    fieldsets = (
        ('Общее', {
            "fields": ("title", "description")
        }),
        ("Финансы",{
            "fields" : ("price", "auction"),
            "classes": ["collapse"] # чтобы можно было  сворачивать поле
        })
    )

    @admin.action(description="Отключить возможность торгов")
    def set_auction_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description="Включение возможность торгов")
    def set_auction_true(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisement, ApplicationAdmin)
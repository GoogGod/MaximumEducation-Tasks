from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "description", "price", "created_date", "auction", "updated_date", "mini_image"]
    list_filter = ["auction", "created_at"] # добавляем возможность фильтрации
    actions = ["make_auction_as_false", "make_auction_as_true"] # чтобы action работал, для него нужно создать функцию

    # добавляет разделение на подразделы при добавлении нового объекта
    fieldsets = (
        ('Общее', {
            "fields": ("title", "description", "user", "image")
        }),
        ("Финансы",{
            "fields" : ("price", "auction"),
            "classes": ["collapse"] # чтобы можно было  сворачивать поле
        })
    )

    # название функции такое же как указано в actions
    # декоратор - дополняет функцию
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset): #request - запрос, queryset- набор объектов, с которыми надо сделать action
        queryset.update(auction = False)

    # сам задание - сделать наоборот - включение торгов
    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset): #request - запрос, queryset- набор объектов, с которыми надо сделать action
        queryset.update(auction = True)


# управляем классом Advertisement через класс AdvertisementAdmin
admin.site.register(Advertisement, AdvertisementAdmin)
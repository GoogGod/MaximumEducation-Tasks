from django.db import models
from django.contrib import admin
# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    auction = models.BooleanField("Торг")
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add - дает now время когда был создан элемент
    updated_at = models.DateTimeField(auto_now=True) # auto_now - при любом изменении

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"

    # Заказчик попросил, чтобы если объявление было создано сегодня,
    # то должно отображаться: "Сегодня в 11:31:46"
    # а сейчас у нас вот так: "04.08.2023 в 11:31:46"
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            # тэг - это элемент в html
            # тэг span - односрочный текст
            return html.format_html(
                "<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", created_time
            )
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")
    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            # тэг - это элемент в html
            # тэг span - односрочный текст
            return html.format_html(
                "<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")
from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    auction = models.BooleanField("Торг")
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add - дает now время при создании
    updated_at = models.DateTimeField(auto_now=True) # auto_now - при любом изменении

    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"
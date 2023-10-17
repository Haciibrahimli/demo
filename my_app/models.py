from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="daxil edilecek ad")
    surname = models.CharField(max_length=255, verbose_name="daxil edilecek soyad")
    age = models.CharField(max_length=255, verbose_name="daxil edilecek yas")
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    

    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ("add_date",)
        verbose_name = "daxil edilecek ad"
        verbose_name_plural = "daxil edilecek adlar"

    


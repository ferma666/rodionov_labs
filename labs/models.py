from django.db import models


class ProfessionCategory(models.Model):
    name = models.CharField(verbose_name="Наименование категории профессии", max_length=255)

    class Meta:
        verbose_name = "Категория профессий"
        verbose_name_plural = "Категории профессий"

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(verbose_name="Наименование профессии", unique=True, max_length=255)
    count = models.IntegerField(verbose_name="Количество работников данной професии")
    first_shift_count = models.IntegerField(verbose_name="Количество работников в первую смену")
    category = models.ForeignKey(ProfessionCategory, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.name

    def get_data(self):
        data = {
            'id': self.pk,
            'name': self.name,
            'count': self.count,
            'first_shift_count': self.first_shift_count,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None
        }
        return data

from django.db import models

class Portfolio(models.Model):
    title = models.CharField("عنوان پروژه", max_length=255)
    category = models.CharField("دسته‌بندی", max_length=100)
    image = models.ImageField("تصویر", upload_to='portfolio/')
    link = models.URLField("لینک جزئیات", blank=True, null=True)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    class Meta:
        verbose_name = "نمونه‌کار"
        verbose_name_plural = "نمونه‌کارها"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

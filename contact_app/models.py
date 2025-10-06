from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("نام و نام خانوادگی", max_length=150)
    email = models.EmailField("ایمیل", blank=True, null=True)
    phone = models.CharField("شماره تماس", max_length=20, blank=True, null=True)
    subject = models.CharField("موضوع", max_length=200)
    message = models.TextField("پیام")
    created_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} - {self.subject}"

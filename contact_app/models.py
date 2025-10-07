from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField("نام و نام خانوادگی", max_length=100)
    email = models.EmailField("آدرس ایمیل", blank=True, null=True)
    subject = models.CharField("موضوع", max_length=200)
    message = models.TextField("پیام")
    created_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس با ما"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

from django.db import models

from django.db import models

class HeroSection(models.Model):
    button_text = models.CharField("متن دکمه", max_length=255)
    title = models.CharField("عنوان اصلی", max_length=255)
    subtitle = models.CharField("زیرعنوان", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "بخش هدر سایت"
        verbose_name_plural = "بخش‌های هدر سایت"

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField("نام برند", max_length=255)
    logo = models.ImageField("لوگوی برند", upload_to="brands/")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.name

class ProductPlan(models.Model):
    title = models.CharField("عنوان پلن", max_length=255)
    price = models.PositiveIntegerField("قیمت (تومان)")
    per_month = models.BooleanField("پرداخت ماهانه", default=True)
    description = models.TextField("توضیحات کوتاه", blank=True, null=True)
    features = models.TextField("ویژگی‌ها (هر خط یک ویژگی)", blank=True, null=True)
    is_popular = models.BooleanField("محبوب", default=False)
    button_text = models.CharField("متن دکمه", max_length=100, default="اکنون بخرید")
    button_link = models.URLField("لینک دکمه", default="#")

    class Meta:
        verbose_name = " محصول"
        verbose_name_plural = " محصولات"

    def get_features_list(self):
        return self.features.splitlines() if self.features else []

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField("نام شخص", max_length=255)
    role = models.CharField("سمت/شرکت", max_length=255)
    avatar = models.ImageField("تصویر کاربر", upload_to="testimonials/")
    message = models.TextField("متن نظر")
    link = models.URLField("لینک", blank=True, null=True)

    class Meta:
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظرات مشتریان"

    def __str__(self):
        return f"{self.name} - {self.role}"

class FAQ(models.Model):
    question = models.CharField("سؤال", max_length=255)
    answer = models.TextField("پاسخ")

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.question

class Feature(models.Model):
    title = models.CharField("عنوان ویژگی", max_length=255)
    description = models.TextField("توضیحات")
    icon = models.ImageField("آیکون (تصویر)", upload_to="features/")
    link = models.URLField("لینک", default="#")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی‌ها"

    def __str__(self):
        return self.title

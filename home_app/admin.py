from django.contrib import admin
from .models import HeroSection , Brand , ProductPlan, Testimonial ,FAQ , Feature

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "logo",)

@admin.register(ProductPlan)
class ProductPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_popular")
    list_editable = ("is_popular",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "link")

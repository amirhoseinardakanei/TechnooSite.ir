from django.shortcuts import render
from .models import HeroSection, Brand, ProductPlan, Feature, Testimonial, FAQ

def site_header_partial(request):
    hero = HeroSection.objects.first()
    return render(request, "site_header_component.html", {"hero": hero})

def site_footer_partial(request):
    hero = HeroSection.objects.first()
    return render(request, "site_footer_component.html", {"hero": hero})

def home(request):
    hero = HeroSection.objects.first()
    brands = Brand.objects.all().order_by("id")
    plans = ProductPlan.objects.all().order_by("price")
    features = Feature.objects.all().order_by("id")
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    return render(request, "index.html", {
        "hero": hero,
        "brands": brands,
        "plans": plans,
        "features": features,
        "testimonials": testimonials,
        "faqs": faqs,
    })

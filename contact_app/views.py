from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد ✅")
            return redirect('contact')
        else:
            messages.error(request, "لطفاً تمام فیلدها را به‌درستی پر کنید ❌")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

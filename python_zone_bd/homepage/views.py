from django.shortcuts import render, redirect
from products.models import Product
from django.contrib import messages
from products.forms import ContactForm
from .models import FAQ
# Create your views here.
def homepage(request):
    products = Product.objects.filter(available=True)
    faqs = FAQ.objects.all()
    context = {
        "products": products,
        "faqs": faqs,
    }
    return render(request, 'products/homepage.html', context )


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {"products": products})


def about(request):
    return render(request, "products/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves message to database
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # redirects to same page
    else:
        form = ContactForm()
    return render(request, "products/contact.html", {"form": form})

def faq(request):
    faqs = FAQ.objects.all()
    context = {
        "faqs": faqs,
    }
    return render(request, "products/faq.html", context)


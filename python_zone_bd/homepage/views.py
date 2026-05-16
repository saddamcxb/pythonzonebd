from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, ProductImage, ContactMessage
from django.contrib import messages
from products.forms import ContactForm
from .models import FAQ

def homepage(request):
    products = Product.objects.filter(available=True)
    faqs = FAQ.objects.all()
    return render(request, 'products/homepage.html', {
        "products": products,
        "faqs": faqs,
    })


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {"product": product})


def about(request):
    return render(request, "products/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, "products/contact.html", {"form": form})


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, "products/faq.html", {"faqs": faqs})


# views.py - পেমেন্ট ভিউ

import requests
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# class BkashPaymentGateway:
#     """বিকাশ পেমেন্ট গেটওয়ে ক্লাস"""
    
#     def __init__(self):
#         self.base_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta"  # স্যান্ডবক্স URL
#         self.username = "your_username"  # আপনার মার্চেন্ট ইউজারনেম
#         self.password = "your_password"  # আপনার মার্চেন্ট পাসওয়ার্ড
#         self.app_key = "your_app_key"    # আপনার অ্যাপ কী
#         self.app_secret = "your_app_secret"  # আপনার অ্যাপ সিক্রেট
        
#     def get_token(self):
#         """পেমেন্টের জন্য টোকেন জেনারেট করুন"""
#         url = f"{self.base_url}/tokenized/checkout/token/grant"
#         headers = {
#             'Content-Type': 'application/json',
#             'username': self.username,
#             'password': self.password
#         }
#         body = {
#             'app_key': self.app_key,
#             'app_secret': self.app_secret
#         }
        
#         response = requests.post(url, json=body, headers=headers)
#         if response.status_code == 200:
#             return response.json()['id_token']
#         return None
    
#     def create_payment(self, amount, order_id):
#         """পেমেন্ট তৈরি করুন"""
#         token = self.get_token()
#         if not token:
#             return None
            
#         url = f"{self.base_url}/tokenized/checkout/create"
#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': token,
#             'X-APP-Key': self.app_key
#         }
#         body = {
#             'mode': '0011',
#             'payerReference': order_id,
#             'callbackURL': 'https://pythonzonebd.com/payment/callback/',
#             'amount': amount,
#             'currency': 'BDT',
#             'intent': 'sale',
#             'merchantInvoiceNumber': order_id
#         }
        
#         response = requests.post(url, json=body, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         return None

# @csrf_exempt
# def bkash_payment(request):
#     """পেমেন্ট পৃষ্ঠা"""
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         amount = request.POST.get('amount')
#         order_id = f"ORDER{product_id}{request.user.id}"
        
#         # পেমেন্ট তৈরি করুন
#         bkash = BkashPaymentGateway()
#         payment = bkash.create_payment(amount, order_id)
        
#         if payment and payment.get('bkashURL'):
#             return redirect(payment['bkashURL'])
#         else:
#             return render(request, 'payment_error.html', {'error': 'পেমেন্ট তৈরি হয়নি'})
    
#     return render(request, 'products/payment/payment_page.html')

# @csrf_exempt
# def payment_callback(request):
#     """পেমেন্ট কলব্যাক URL"""
#     if request.method == 'POST' or request.method == 'GET':
#         status = request.GET.get('status')
#         payment_id = request.GET.get('paymentID')
        
#         if status == 'success':
#             # পেমেন্ট সফল হয়েছে
#             # এখানে অর্ডার কনফার্ম করুন এবং প্রোডাক্ট ডাউনলোড দিন
#             return render(request, 'payment_success.html', {'payment_id': payment_id})
#         else:
#             # পেমেন্ট ব্যর্থ হয়েছে
#             return render(request, 'payment_failed.html')
    
#     return JsonResponse({'error': 'Invalid request'}, status=400)
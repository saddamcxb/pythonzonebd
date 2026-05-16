from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products/", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    # path('payment/bkash/', views.bkash_payment, name='bkash_payment'),
]


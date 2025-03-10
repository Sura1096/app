import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        "currency": "usd",
                        "product_data": {"name": item.name},
                        "unit_amount": item.price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"session_id": checkout_session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)

    return render(request, "item.html", {"item": item, "stripe_public_key": settings.STRIPE_PUBLIC_KEY})


def buy_order(request, id):
    order = get_object_or_404(Order, id=id)

    line_items = [
        {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item.name},
                "unit_amount": item.price,
            },
            "quantity": 1,
        }
        for item in order.items.all()
    ]

    # Добавляем скидку
    discounts = []
    if order.discount:
        discount = stripe.Coupon.create(
            name=order.discount.name,
            amount_off=order.discount.amount,
            currency="usd",
        )
        discounts.append({"coupon": discount.id})

    # Добавляем налог
    tax_rates = []
    if order.tax:
        tax_rate = stripe.TaxRate.create(
            display_name=order.tax.name,
            percentage=order.tax.percentage,
            inclusive=False,
        )
        tax_rates.append(tax_rate.id)

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/success",
            cancel_url="http://localhost:8000/cancel",
            discounts=discounts,
            tax_id_collection={"enabled": True} if order.tax else {},
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"session_id": checkout_session.id})

from django.contrib.auth.models import User
from django.core.mail import send_mail
import os


def verify_email(stock_history, stock, user):
    current_price = stock_history.price
    min_value = stock.min_value
    max_value = stock.max_value

    if (current_price <= min_value):
        send_buy_email(stock, user)
    elif (current_price >= max_value):
        send_sell_email(stock, user)


def send_buy_email(stock, user: User):
    subject = 'Buy a stock'
    message = f"You can buy the stock {stock.symbol}"
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to_emails = [user.email]

    send_mail(subject, message, from_email, to_emails)


def send_sell_email(stock, user):
    subject = 'You can sell a stock'
    message = f"You can sell the stock {stock.symbol}"
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to_emails = [user.email]

    send_mail(subject, message, from_email, to_emails)
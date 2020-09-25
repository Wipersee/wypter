from __future__ import absolute_import, unicode_literals
from celery import task
from .models import MonthlyExtend, Wallet, Extend
from decimal import Decimal
from datetime import datetime, timedelta

def wallet_write_off(extend):
    user_wallet = Wallet.objects.get(pk=extend.wallet.id)
    if user_wallet.balance - extend.price < 0:
        pass
    else:
        user_wallet.balance=Decimal(
                            user_wallet.balance) - Decimal(extend.price)
        user_wallet.save()
        ex = Extend.objects.create(
            category=extend.category,
            price=extend.price,
            comment=f'Monthly extend {extend.description}',
            wallet=user_wallet
        )
        ex.save()


@task()
def monthly_extend_check():
    m_extends = MonthlyExtend.objects.filter(date=datetime.now().strftime('%d'))
    for i in list(m_extends):
        wallet_write_off(i)

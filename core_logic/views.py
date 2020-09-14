from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddExtendForm, AddIncomeForm
from .models import Wallet, Extend, Income, Category
from account.models import Profile
from decimal import Decimal
from django.db.models import Sum
from datetime import datetime, timedelta


@login_required
def dashboard(request):
    if request.method == "POST":
        if 'btn_extend' in request.POST:
            extend_form = AddExtendForm(request.POST)
            if extend_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                if user_wallet.balance - extend_form.cleaned_data['price'] < 0:
                    return render(request, 'core_logic/main_stat.html',
                                  {'active': 'dashboard',
                                             'extend_form': extend_form,
                                             'income_form': AddIncomeForm(),
                                             'wallet': user_wallet,
                                             'sum_extends': Decimal(sum([x.price for x in Extend.objects.filter(wallet=user_wallet)])),
                                             'error': True})
                else:
                    user_wallet.balance = Decimal(
                        user_wallet.balance) - Decimal(extend_form.cleaned_data['price'])
                    user_wallet.save()
                    ex = Extend.objects.create(category=extend_form.cleaned_data['category'],
                                               price=extend_form.cleaned_data['price'],
                                               comment=extend_form.cleaned_data['comment'],
                                               wallet=user_wallet)
                    ex.save()
                    return redirect('/')
        elif 'btn_income' in request.POST:
            income_form = AddIncomeForm(request.POST)
            if income_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                user_wallet.balance = Decimal(
                    user_wallet.balance) + Decimal(income_form.cleaned_data['price'])
                user_wallet.save()
                inc = Income.objects.create(
                    price=income_form.cleaned_data['price'],
                    wallet=user_wallet)
                inc.save()
                return redirect('/')
    else:
        extend_form = AddExtendForm()
        income_form = AddIncomeForm()
        user_wallet = Wallet.objects.get(
            user=Profile.objects.get(user=request.user))
        sum_extends = [
            x.price for x in Extend.objects.filter(wallet=user_wallet)]
        return render(request, 'core_logic/main_stat.html',
                      {'active': 'dashboard',
                                 'extend_form': extend_form,
                                 'income_form': income_form,
                                 'wallet': user_wallet,
                       'sum_extends': Decimal(sum(sum_extends)), })


@login_required
def pie_chart(request):
    if request.method == "POST":
        if 'btn_extend' in request.POST:
            extend_form = AddExtendForm(request.POST)
            if extend_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                if user_wallet.balance - extend_form.cleaned_data['price'] < 0:
                    return render(request, 'core_logic/main_stat.html',
                                  {'active': 'dashboard',
                                             'extend_form': extend_form,
                                             'income_form': AddIncomeForm(),
                                             'wallet': user_wallet,
                                             'sum_extends': Decimal(sum([x.price for x in Extend.objects.filter(wallet=user_wallet)])),
                                             'error': True})
                else:
                    user_wallet.balance = Decimal(
                        user_wallet.balance) - Decimal(extend_form.cleaned_data['price'])
                    user_wallet.save()
                    ex = Extend.objects.create(category=extend_form.cleaned_data['category'],
                                               price=extend_form.cleaned_data['price'],
                                               comment=extend_form.cleaned_data['comment'],
                                               wallet=user_wallet)
                    ex.save()
                    return redirect('pie_chart')
        elif 'btn_income' in request.POST:
            income_form = AddIncomeForm(request.POST)
            if income_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                user_wallet.balance = Decimal(
                    user_wallet.balance) + Decimal(income_form.cleaned_data['price'])
                user_wallet.save()
                inc = Income.objects.create(
                    price=income_form.cleaned_data['price'],
                    wallet=user_wallet)
                inc.save()
                return redirect('pie_chart')
    else:
        extend_form = AddExtendForm()
        income_form = AddIncomeForm()
        user_wallet = Wallet.objects.get(
            user=Profile.objects.get(user=request.user))
        user_wallet = Wallet.objects.get(
            user=Profile.objects.get(user=request.user))

        # Raw sql statement to return queryset group by ctegories
        date_buffer = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        query = f'''SELECT core_logic_extend.id, core_logic_extend.category_id, 
        SUM(core_logic_extend.price) as price, core_logic_category.name, core_logic_extend.wallet_id, core_logic_extend.date
        FROM core_logic_extend 
        INNER JOIN core_logic_category 
        ON core_logic_extend.category_id = core_logic_category.id 
        WHERE core_logic_extend.date >= '{date_buffer}' AND core_logic_extend.wallet_id = {user_wallet.id}  
        GROUP BY core_logic_category.name         
        ORDER BY core_logic_extend.price DESC;'''
        extends = Extend.objects.raw(query)
        return render(request, 'core_logic/pie.html', {'active': 'pie',
                                                       'extends': extends,
                                                       'wallet': user_wallet,
                                                       'extend_form': extend_form,
                                                       'income_form': income_form, })


@login_required
def graph_chart(request):
    if request.method == "POST":
        if 'btn_extend' in request.POST:
            extend_form = AddExtendForm(request.POST)
            if extend_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                if user_wallet.balance - extend_form.cleaned_data['price'] < 0:
                    return render(request, 'core_logic/main_stat.html',
                                  {'active': 'dashboard',
                                             'extend_form': extend_form,
                                             'income_form': AddIncomeForm(),
                                             'wallet': user_wallet,
                                             'sum_extends': Decimal(sum([x.price for x in Extend.objects.filter(wallet=user_wallet)])),
                                             'error': True})
                else:
                    user_wallet.balance = Decimal(
                        user_wallet.balance) - Decimal(extend_form.cleaned_data['price'])
                    user_wallet.save()
                    ex = Extend.objects.create(category=extend_form.cleaned_data['category'],
                                               price=extend_form.cleaned_data['price'],
                                               comment=extend_form.cleaned_data['comment'],
                                               wallet=user_wallet)
                    ex.save()
                    return redirect('grah_chart')
        elif 'btn_income' in request.POST:
            income_form = AddIncomeForm(request.POST)
            if income_form.is_valid():
                user_wallet = Wallet.objects.get(
                    user=Profile.objects.get(user=request.user))
                user_wallet.balance = Decimal(
                    user_wallet.balance) + Decimal(income_form.cleaned_data['price'])
                user_wallet.save()
                inc = Income.objects.create(
                    price=income_form.cleaned_data['price'],
                    wallet=user_wallet)
                inc.save()
                return redirect('graph_chart')
    else:
        extend_form = AddExtendForm()
        income_form = AddIncomeForm()
        user_wallet = Wallet.objects.get(
            user=Profile.objects.get(user=request.user))
        user_wallet = Wallet.objects.get(
            user=Profile.objects.get(user=request.user))
        extends = Extend.objects.filter(wallet=user_wallet, date__gte = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')).values(
            'date').annotate(price=Sum('price'))[::-1]
    return render(request, 'core_logic/graph.html', {'active': 'graph',
                                                     'extends': extends,
                                                     'wallet': user_wallet,
                                                     'extend_form': extend_form,
                                                     'income_form': income_form, })

def detail_sum(request):
    wallet = Wallet.objects.get(user=Profile.objects.get(user=request.user))
    extends = Extend.objects.filter(wallet=wallet).order_by('-date')
    return render(request, 'core_logic/detail.html', {'extends': extends,
                                                      'wallet': wallet})

def delete_extension(request):
    pass
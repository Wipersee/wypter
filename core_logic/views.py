from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddExtendForm, AddIncomeForm
from .models import Wallet

# Create your views here.
@login_required
def dashboard(request):
	"""if request.method = "POST":
		extend_form = AddExtendForm(instance=request.Extend,data=request.POST)
		income_form = AddIncomeForm(instance=request.Income,data=request.POST)
		if extend_form.is_valid() or income_form.is_valid():
			wallet = Wallet.objects.get(user=request.user)
			if wallet.ballance - int(extend_form['price']) < 0:"""
	return render(request,'core_logic/main_stat.html', {'active':'dashboard'})

@login_required
def pie_chart(request):
    return render(request, 'core_logic/pie.html', {'active': 'pie'})

@login_required
def graph_chart(request):
    return render(request, 'core_logic/graph.html', {'active': 'graph'})
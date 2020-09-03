from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'core_logic/main_stat.html', {'active':'dashboard'})

@login_required
def pie_chart(request):
    return render(request, 'core_logic/pie.html', {'active': 'pie'})

@login_required
def graph_chart(request):
    return render(request, 'core_logic/graph.html', {'active': 'graph'})
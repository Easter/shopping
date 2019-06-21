from django.shortcuts import render,get_object_or_404
from .models import Commodity
from user.models import User
from .forms import CommodityForm
from user.models import User_commodity
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    commodities = Commodity.objects.all()
    return render(request, "shopping/index.html", {'commodities':commodities})

def delete(request,user_pk,commodity_pk):
    user = User.objects.get(pk=user_pk)
    # commodity_test = Commodity.objects.get(=commodity_pk)
    if user.username == 'admin':
        commodity = get_object_or_404(Commodity,pk=commodity_pk)
        commodity.delete()
        commodities = Commodity.objects.all()
        return render(request, 'shopping/index.html', {'commodities': commodities, "user": user})
    else:
        commodity = get_object_or_404(User_commodity, pk=commodity_pk)
        commodity.delete()
        user = User.objects.get(pk=user_pk)
        user_comms = User_commodity.objects.filter(user=user)
        return render(request, 'user/commodities.html', {'commodities':user_comms,"user":user})

def deleteAll(request,user_pk):
    user = User.objects.get(pk=user_pk)
    commodities = User_commodity.objects.filter(user=user)
    commodities.delete()
    user_comms = User_commodity.objects.filter(user=user)
    # print(user_comms)
    # commodities = []
    # for user_comm in user_comms:
    #     commodities.append(user_comm.commodity)
    return render(request,'user/commodities.html',{'commodities': user_comms,"user": user})

@csrf_exempt
def add(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CommodityForm(request.POST)
        if form.is_valid():
            commodity = form.save(commit=False)
            commodity.save()
            commodities = Commodity.objects.all()
            return render(request,'shopping/index.html',{'commodities': commodities,"user": user})


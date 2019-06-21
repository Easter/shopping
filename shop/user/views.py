from django.shortcuts import render,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .forms import UserForm
from .models import User,User_commodity
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from shopping.models import Commodity
from django.db.models import Q
import shopping.urls
import json
# Create your views here.

def index(request):
    return render(request,'user/init.html')
def login(request):
    return render(request,'user/index.html')

def logon(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        if username == "admin":
            pwd = request.POST.get("password")
            user = User.objects.get(username=username)
            password = User.objects.filter(username=username).values("password")[0].get("password")
            if pwd == password:
                pk = user.pk
                user = User.objects.get(pk=pk)
                commodities = Commodity.objects.all()
                return render(request, "shopping/index.html", {"commodities": commodities, "user": user})
            else:
                error_msg = "密码错误"
                return render(request, "user/index.html", {"error_msg": error_msg})
        else:
            pwd = request.POST.get("password")
            try:
                user = User.objects.get(username=username)
                password = User.objects.filter(username=username).values("password")[0].get("password")
                print(password)
                if pwd == password:
                    pk = user.pk
                    user = User.objects.get(pk=pk)
                    user_comms = User_commodity.objects.filter(user=user)
                    # print(user_comms)
                    # commodities = []
                    # for user_comm in user_comms:
                    #     commodities.append(user_comm.commodity)
                    return render(request, "user/commodities.html",{"commodities": user_comms,"user":user})
                else:
                    error_msg = "密码错误"
                    return render(request,"user/index.html",{"error_msg": error_msg})
            except ObjectDoesNotExist:
                error_msg = "登陆失败，可能是用户或者密码错误"
                return render(request,"user/index.html",{"error_msg": error_msg})

def apply(request):
    if request.method == 'POST':
        print("方法为post")
        form = UserForm(request.POST)
        try:
            username = request.POST.get("username")
            user = User.objects.get(username=username)
            if(user):
                error_msg = "用户名已存在"
                return render(request, 'user/index.html', {"error_msg": error_msg})
        except ObjectDoesNotExist:
            user = form.save(commit=False)
            user.save()
            error_msg = "注册成功请登陆"
            return render(request, "user/index.html",{"error_msg": error_msg})

def search(request,pk):
    q = request.GET.get("q")
    error_msg = ""

    if not q:
        error_msg = "请输入关键词"
        return render(request,'user/commodities.html',{"error_msg":error_msg})
    commodities = Commodity.objects.filter(Q(name__icontains=q))
    user = User.objects.get(pk=pk)
    # Q提供了更复杂的搜索方式不用Q的话就只能写成逗号分隔的格式，表达意思为且
    return render(request,"user/add_commodities.html",{"commodities": commodities,"user":user})

def add(request,commodity_pk,user_pk):
    commodity = get_object_or_404(Commodity, pk=commodity_pk)
    print(commodity.name)
    user = User.objects.get(pk=user_pk)
    object = User_commodity()
    object.commodity = commodity
    object.user = user
    object.save()
    user_comms = User_commodity.objects.filter(user=user)
    # print(user_comms)
    # commodities = []
    # for user_comm in user_comms:
    #     commodities.append(user_comm.commodity)
    return render(request,"user/commodities.html",{"commodities": user_comms,"user":user})


def number_add(request):
    print("运行到了这里")
    # if request.method == 'POST':
    number = request.GET.get("number")
    id = request.GET.get("id")
    user = User_commodity.objects.get(id=id)
    print("number值：" + str(number))
    print("number类型:" + str(type(number)))
    number  = int(number)
    number += 1
    user.number = number
    user.save()
    # number = 100
    return_json = {'result': number}
    return HttpResponse(json.dumps(return_json), content_type='application/json')

def number_sub(request):
    print("运行到了这里")
    # if request.method == 'POST':
    number = request.GET.get("number")
    id = request.GET.get("id")
    user = User_commodity.objects.get(id=id)
    print("number值：" + str(number))
    print("number类型:" + str(type(number)))
    number  = int(number)
    number -= 1
    user.number = number
    user.save()
    # number = 100
    return_json = {'result': number}
    return HttpResponse(json.dumps(return_json), content_type='application/json')






import json

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django_bootstrap_table_web.models import User
from django_bootstrap_table_web.models import user2dict
from .forms import UserForm


# Create your views here.

def user(request):
    if request.method == "GET":
        user_id = request.GET.get('id')
        if user_id and int(user_id) > 0:
            user_id = int(user_id)
            user_form = UserForm(instance=User.objects.get(pk=user_id))
        else:
            user_form = UserForm()
        return render(request, "user/add.html", {"user_form": user_form, "user_id": user_id})
    elif request.method == "POST":
        user_id = request.POST.get("id", 0)
        if user_id and int(user_id) > 0:
            user_id = int(user_id)
            message = "修改成功"
            form = UserForm(request.POST, instance=User.objects.get(pk=user_id))
        else:
            message = "添加成功"
            form = UserForm(request.POST)
        if form.is_valid():
            is_save = True
        if is_save:
            form.save()
        else:
            print("error:", form.errors)
            message = form.errors
        return render(request, "user/add.html", {"message": message, "user_id": user_id})
    else:
        pass


def test(request):
    data = {
        "name": "hello",
        "sex": "男",
        "request": request
    }
    return render(request, 'test.html', data)


# 用户详情
def detail(request, id=None):
    if not id:
        if not request.GET.get("id"):
            id = None
        else:
            id = request.GET.get("id")
    pass
    u = None
    try:
        u = user2dict(User.objects.get(id=id))
    except Exception as err:
        print("err:", err)
    return HttpResponse(json.dumps(u), content_type="application/json")


# 返回user json数据
def user_list(request):
    limit, offset = [None, None]
    if "limit" in request.GET:
        limit = request.GET["limit"]
    if "offset" in request.GET:
        offset = request.GET["offset"]
    print("limit:{},offset:{}".format(limit, offset))
    users = User.objects.all()
    rows = []
    for user in users:
        rows.append(user2dict(user))
    data = {
        "total": User.objects.count(),
        "rows": rows
    }
    print("data:", data)
    return HttpResponse(json.dumps(data), content_type="application/json")


def newdata(request):
    data = {
        "newcount": User.objects.count(),
        "username": "admin"
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def datacount(request):
    data = {
        "d": 10,
        "c": ["2018-02-04"]
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def hello(request):
    print("aaa")
    return HttpResponse("hello world!")


# redirect响应
def redirect(request):
    return HttpResponseRedirect(reverse("django_bootstrap_table:detail", args=(1,)))

#coding:utf-8
import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render
from Monitor.models import *
from AuthoriseManager.models import *

def hashpassword(password):
    """
     本系统采用hash md5 加密的方式对登录密码进行加密
    """
    h = hashlib.md5()
    h.update(password)
    return h.hexdigest()

def user_valid(user_code,passwd):
    try:
        user = User.objects.get(user_code=user_code)
        # if user.password == hashpassword(passwd):
        if user.password == passwd:
            return True
        else:
            return False
    except:
        return False

def login_valid(func): #这是一个装饰器的函数，外层的函数是用来接收被装饰函数的的
    def inner(request,*args,**kwargs):
        try:
            username = request.session["user_code"] #尝试获取session
            return func(request, *args, **kwargs)#index(request) 如果获取到执行被装饰函数
        except KeyError as e: #否则返回404页面
            if repr(e) == "KeyError('user_code',)":
                err = "当前用户未登录请登录"
            else:
                err = str(e)
            url = "/404/"+err
            return HttpResponseRedirect(url)
    return inner

def login(request):
    result = {}
    if request.method == 'POST' and request.POST:
        user_code = request.POST.get('user_code', '')
        password = request.POST.get('password', '')
        if user_code and password and user_valid(user_code,password):
            response = HttpResponseRedirect('/')
            response.set_cookie('user_code',user_code)
            request.session['user_code'] = user_code
            return response
        else:
            result["error"] = "用户名或者密码错误"
            return render(request, 'login/login.html', locals())
    return render(request, 'login/login.html', locals())

@login_valid
def index(request):
    host_num = HostInfo.objects.count()
    table_list = HostInfo.objects.all()
    return render(request, 'index.html', locals())

def err_404(request, error_content):
    return render(request, '404.html', locals())

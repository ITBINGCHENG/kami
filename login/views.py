from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from . import models
from . import forms

# Create your views here.

def index(request):
    if request.session.get('is_login')==True:
        user = models.User.objects.get(name=request.session['user_name'])
        try:
            kamiid = user.kamiid
            kami = models.Kami.objects.get(kamiid= kamiid)
            kami = kami.kamizhi.split('@#')#列表
        except:
            kami = ["未找到，请等待十分钟或联系卖家"]

    return render(request, 'login/index.html',locals())


# login/views.py

def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "订单号不存在！"
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")




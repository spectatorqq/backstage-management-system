from django.db.models import Count
from django.shortcuts import render
from mana.models import TUser
# Create your views here.

import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mana.models import TCarousel


# Create your views here.


@csrf_exempt
def save_user(request):
    realname = request.POST.get('realname')
    nickname = request.POST.get('nickname')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    number = request.POST.get('number')
    password = request.POST.get('password')
    status = request.POST.get('status')
    location = request.POST.get('location')
    sign = request.POST.get('sign')
    reg_date = request.POST.get('reg_date')
    pic = request.FILES.get('pic')
    print('realname', realname, 'pic', pic, 'status', status)
    try:
        TUser.objects.create(realname=realname, nickname=nickname, age=age, gender=gender, number=number,
                             password=password, user_status=status, location=location, sign=sign, reg_date=reg_date,
                             portrait_url=pic)
        return HttpResponse('ok')
    except:
        pass
    return HttpResponse('failed')


def show_current_page(request):
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    print('show current page')
    user_list = TUser.objects.all().order_by("id")
    print(user_list)
    all_page = Paginator(user_list, rows_num)
    page = all_page.page(page_num)

    rows = []
    for i in page:
        rows.append(i)

    data = {
        "page": page_num,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": rows,
    }

    def my_default(u):
        if isinstance(u, TUser):
            return {"id": u.id,
                    "realname": u.realname,
                    "nickname": u.nickname, 
                    "age": u.age,
                    "gender": u.gender,
                    "number": u.number,
                    "password": u.password,
                    "status": u.user_status,
                    "location": u.location,
                    "sign": u.sign,
                    "reg_date": u.reg_date.strftime("%Y-%m-%d"),
                    "pic": u.portrait_url.url,
                    }

    user_json = json.dumps(data, default=my_default)

    return HttpResponse(user_json)


@csrf_exempt
def edit_user(request):
    """
    编辑用户时所使用的方法
    :param request: 判断执行方式  表单参数
    :return:
    """
    
    opt = request.POST.get("oper")
    realname = request.POST.get('realname')
    nickname = request.POST.get('nickname')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    number = request.POST.get('number')
    password = request.POST.get('password')
    status = request.POST.get('status')
    location = request.POST.get('location')
    sign = request.POST.get('sign')
    reg_date = request.POST.get('reg_date')
    pic_id = request.POST.get("id")
    
    if opt == "del":
        TUser.objects.get(pk=pic_id).delete()
    elif opt == "edit":
        u = TUser.objects.all().get(pk=pic_id)
        u.realname = realname
        u.nickname = nickname
        u.age = age
        u.gender = gender
        u.number = number
        u.password = password
        u.user_status = status
        u.location = location
        u.sign = sign
        u.reg_date = reg_date
        u.save()
    
    return HttpResponse("成功")


def get_map_data(request):
    users = TUser.objects.values('location').annotate(Count('id'))
    data = []
    for u in users:
        d = {'name': u['location'], 'value': u['id__count']}
        data.append(d)
    # print(data)
    return JsonResponse(data, safe=False)


def get_data(request):
    users = TUser.objects.order_by('reg_date').values('reg_date').annotate(Count('id'))
    data = {
        'name': [],
        'value': []
    }
    for u in users:
        data['name'].append(u['reg_date'])
        data['value'].append(u['id__count'])

    # sorted(data, key=lambda x: x['name'])
    print(data)
    return JsonResponse(data, safe=False)


def test(request):
    return render(request, '../static/static_html/test.html')

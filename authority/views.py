# Create your views here.
import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from authority.models import Staff
from utils.permission_to_session import save_permission


def show_current_staff(request):
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    staff_list = Staff.objects.all().order_by("id")
    all_page = Paginator(staff_list, rows_num)
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
        if isinstance(u, Staff):
            return {"id": u.id,
                    'name': u.name,
                    'password': u.password,
                    'role': ','.join([x['title'] for x in u.role.values('title')])
                    }

    staff_json = json.dumps(data, default=my_default)

    return HttpResponse(staff_json)


def login(request):

    return render(request, 'staff_login.html')


def login_logic(request):
    if request.method == 'GET':
        return render(request, 'staff_login.html')
    name = request.POST.get('name')
    password = request.POST.get('pwd')
    staff = Staff.objects.filter(name=name, password=password).first()
    if not staff:
        return render(request, 'staff_login.html', {'msg': '用户名或密码错误'})
    # 用户登录成功后将有的权限放入session

    save_permission(staff, request)
    return redirect('/mana/home/')


import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mana.models import TCarousel
# Create your views here.


@csrf_exempt
def save_banner(request):
    pic_name = request.POST.get('name')
    pic_desc = request.POST.get('desc')
    pic_url = request.FILES.get('pic')
    pic_status = request.POST.get('status')
    print(pic_desc, pic_name, pic_status, pic_url)
    try:
        TCarousel.objects.create(img_name=pic_name, img_desc=pic_desc, img_status=pic_status, img_url=pic_url)
        return HttpResponse('ok')
    except:
        pass
    return HttpResponse('failed')


def show_current_page(request):
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    # print('show current page')
    carousel_list = TCarousel.objects.all().order_by("id")

    all_page = Paginator(carousel_list, rows_num)
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

    def my_default(c):
        if isinstance(c, TCarousel):
            return {"id": c.id,
                    "name": c.img_name,
                    "desc": c.img_desc,
                    "url": c.img_url.url,
                    "status": c.img_status,
                    }

    carousel_json = json.dumps(data, default=my_default)

    return HttpResponse(carousel_json)


@csrf_exempt
def edit_carousel(request):
    """
    编辑用户时所使用的方法
    :param request: 判断执行方式  表单参数
    :return:
    """

    opt = request.POST.get("oper")
    pic_name = request.POST.get('name')
    pic_desc = request.POST.get('desc')
    pic_status = request.POST.get('status')
    pic_id = request.POST.get("id")

    if opt == "del":
        TCarousel.objects.get(pk=pic_id).delete()
    elif opt == "edit":
        c = TCarousel.objects.all().get(pk=pic_id)
        c.img_name = pic_name
        c.img_desc = pic_desc
        c.img_status = pic_status
        c.save()

    return HttpResponse("成功")

import os
from mana.models import TUser, TArticleList, TArticlePic
# Create your views here.

import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_article(request):
    title = request.POST.get('title')
    # author_id = request.POST.get('author_id')
    content = request.POST.get('content')
    cate = request.POST.get('cate')
    publish_date = request.POST.get('publish_date')
    article_status = request.POST.get('status')
    # pic = request.FILES.get('pic')
    print('title', title,  'status', article_status)
    try:
        TArticleList.objects.create(title=title,  content=content,
                                    cate=cate, publish_date=publish_date, article_status=article_status,
                                    )
        return HttpResponse('ok')
    except:
        pass
    return HttpResponse('failed')


def show_current_page(request):
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    # print('show current page')
    article_list = TArticleList.objects.all().order_by("id")
    all_page = Paginator(article_list, rows_num)
    page = all_page.page(page_num)
    print(article_list)
    rows = []
    for i in page:
        rows.append(i)

    data = {
        "page": page_num,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": rows,
    }

    def my_default(a):
        if isinstance(a, TArticleList):
            return {
                'id': a.id,
                'title': a.title,
                # 'author_id': a.author_id,
                'cate': a.cate,
                'publish_date': a.publish_date.strftime('%Y-%m-%d'),
                'status': a.article_status,
                'content': a.content,
                    }

    article_json = json.dumps(data, default=my_default)

    return HttpResponse(article_json)


@csrf_exempt
def update_article(request):
    """
    编辑文章时所使用的方法
    :param request: 判断执行方式  表单参数
    :return:
    """

    title = request.POST.get('title')
    # author_id = request.POST.get('author_id')
    content = request.POST.get('content')
    cate = request.POST.get('cate')
    publish_date = request.POST.get('publish_date')
    article_status = request.POST.get('status')
    article_id = request.POST.get("article_id")
    print(article_id)
    a = TArticleList.objects.all().get(pk=article_id)
    print(a)
    a.id = article_id
    a.title = title
    # a.author_id = author_id
    a.content = content
    a.cate = cate
    a.publish_date = publish_date
    a.article_status = article_status
    a.save()

    return HttpResponse("ok")


@csrf_exempt
def del_article(request):
    article_id = request.POST.get('id')
    print(article_id)
    TArticleList.objects.get(pk=article_id).delete()
    return HttpResponse('ok')


@csrf_exempt
def upload_pic(request):
    file = request.FILES.get('imgFile')
    url_suffix = request.scheme + '://' + request.get_host() + '/static/'
    # data = {}
    try:
        try:
            TArticlePic.objects.get(title=file.name)
            data = {"error": 1, "message": "文件重复"}
        except:
            p = TArticlePic.objects.create(title=file.name, pic=file)
            url = url_suffix + p.pic.url
            data = {"error": 0, "url": url}
    except:
        data = {"error": 1, "message": "文件上传失败"}
    return HttpResponse(json.dumps(data), content_type='application/json')


def pic_space(request):
    """
    {
    "moveup_dir_path": "",
    "current_dir_path": "",
    "current_url": "\/ke4\/php\/..\/attached\/",
    "total_count": 5,
    "file_list": [{
        "is_dir": false,
        "has_file": false,
        "filesize": 208736,
        "dir_path": "",
        "is_photo": true,
        "filetype": "jpg",
        "filename": "1241601537255682809.jpg",
        "datetime": "2018-06-06 00:36:39"
    }]
    }
    :param request:
    :return:
    """
    pics = TArticlePic.objects.all()
    url_suffix = request.scheme + '://' + request.get_host() + '/static/'
    file_list = []
    for p in pics:
        p_path, t = os.path.splitext(p.pic.url)
        if os.path.exists(p.pic.path):
            d = {
                "is_dir": False,
                "has_file": False,
                "filesize": p.pic.size,
                "dir_path": "",
                "is_photo": True,
                "filetype": t,
                "filename": p.pic.name,
                "datetime": "2018-06-06 00:36:39"
            }
            file_list.append(d)
        else:
            # print(p.pic.path + '不存在', p.title, p.id)
            TArticlePic.objects.get(title=p.title).delete()
    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": url_suffix,
        "total_count": pics.count(),
        "file_list": file_list
    }

    return HttpResponse(json.dumps(data), content_type='application/json')



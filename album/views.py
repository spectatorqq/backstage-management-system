import json
from django.core import cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mutagen.mp3 import MP3
from mana.models import  TAlbumList, TAudioList
# Create your views here.


@csrf_exempt
def save_album(request):
    album_name = request.POST.get('album_name')
    publish_date = request.POST.get('publish_date')
    album_status = request.POST.get("album_status")
    stars = request.POST.get('stars')
    pic = request.FILES.get('pic')

    TAlbumList.objects.create(album_name=album_name, publish_date=publish_date, album_status=album_status,
                              stars=stars, album_pic_url=pic)
    return HttpResponse('ok')


@csrf_exempt
def save_audio(request):
    audio_name = request.POST.get('audio_name')
    album_id = request.POST.get('album_id')
    audio_status = request.POST.get("audio_status")
    audio_url = request.FILES.get('audio_url')
    m = MP3(audio_url)
    print(m)

    TAudioList.objects.create(audio_name=audio_name, album_id=album_id, audio_status=audio_status,
                              audio_url=audio_url)
    return HttpResponse('ok')


def show_current_page(request):
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    # print('show current page')
    article_list = TAlbumList.objects.all().order_by("id")
    all_page = Paginator(article_list, rows_num)
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

    def my_default(a):
        if isinstance(a, TAlbumList):
            return {
                'id': a.id,
                'album_name': a.album_name,
                'publish_date': a.publish_date.strftime('%Y-%m-%d'),
                'album_status': a.album_status,
                'stars': a.stars,
                'cover': a.album_pic_url.url
            }

    album_json = json.dumps(data, default=my_default)

    return HttpResponse(album_json)


@csrf_exempt
def edit_album(request):
    """
    编辑用户时所使用的方法
    :param request: 判断执行方式  表单参数
    :return:
    """

    opt = request.POST.get("oper")
    album_name = request.POST.get('album_name')
    publish_date = request.POST.get('publish_date')
    album_status = request.POST.get("album_status")
    stars = request.POST.get('stars')
    album_id = request.POST.get("id")

    if opt == "del":
        TAlbumList.objects.get(pk=album_id).delete()
    elif opt == "edit":
        a = TAlbumList.objects.all().get(pk=album_id)
        a.album_name = album_name
        a.publish_date = publish_date
        a.album_status = album_status
        a.stars = stars
        a.save()

    return HttpResponse('ok')


def edit_audio(request):
    """
    编辑用户时所使用的方法
    :param request: 判断执行方式  表单参数
    :return:
    """

    opt = request.POST.get("oper")
    audio_name = request.POST.get('audio_name')
    album_id = request.POST.get('album_id')
    album_status = request.POST.get("album_status")
    audio_id = request.POST.get("id")

    if opt == "delAudio":
        TAudioList.objects.get(pk=audio_id).delete()
    elif opt == "editAudio":
        a = TAlbumList.objects.all().get(pk=audio_id)
        a.audio_name = audio_name
        a.album_id = album_id
        a.album_status = album_status
        a.save()

    return HttpResponse('ok')


def get_audio_by_albumid(request):
    album_id = request.GET.get('album_id')
    rows_num = request.GET.get('rows')
    page_num = request.GET.get('page')
    # print('show current page')
    audio_list = TAudioList.objects.filter(album_id=album_id).order_by('id')
    all_page = Paginator(audio_list, rows_num)
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

    def my_default(a):
        if isinstance(a, TAudioList):
            return {
                'id': a.id,
                'audio_name': a.audio_name,
                'album_id': a.album_id,
                'audio_url': a.audio_url.url,
                'audio_time': a.audio_time,
                'audio_status': a.audio_status,
            }

    audio_json = json.dumps(data, default=my_default)

    return HttpResponse(audio_json)


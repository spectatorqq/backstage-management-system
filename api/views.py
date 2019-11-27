import json
from django.http import QueryDict
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from mana.models import TCarousel, TAlbumList, TArticleList, TAudioList, TUser


class FirstPage(View):

    def get(self, request, *args, **kwargs):
        # u_id = args[0]
        res = {}
        if args[1] == 'all':
            res['header'] = get_all_headers()
            res['album'] = get_all_album()
            res['article'] = get_article(args[2])
        elif args[1] == 'wen':
            res['album'] = get_all_album()
        elif args[1] == 'si':
            res['article'] = get_article(args[2])

        res_json = json.dumps(res)
        print(args)
        return HttpResponse(res_json)


def get_all_headers():
    headers = []
    for c in TCarousel.objects.all():
        temp = {
            'img_name': c.img_name,
            'img_desc': c.img_desc,
            'img_url': c.img_url.url,
            'img_status': c.img_status
        }
        headers.append(temp)
    return headers


def get_all_album():
    album = []
    for a in TAlbumList.objects.all():
        temp = {
            'album': a.album_name,
            'publish_date': a.publish_date.strftime('%Y-%m-%d'),
            'album_state': a.album_status,
            'album_pic_url': a.album_pic_url.url,
        }
        album.append(temp)
    return album


def get_article(cate=""):

    if not cate:
        articles = TArticleList.objects.all()
    else:
        articles = TArticleList.objects.filter(cate=cate)

    article = []
    for w in articles:
        temp = {
            'title': w.title,
            'context': w.content,
            'publish_date': w.publish_date.strftime('%Y-%m-%d')
        }
        article.append(temp)
    return article


class DetailWen(View):

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args: 第一个参数为UID， 第二个参数为albumID
        :param kwargs:
        :return:
        """
        album_list = get_album_audio(args[1])

        album_json = json.dumps(album_list)
        return HttpResponse(album_json)


def get_album_audio(id):
    album = TAlbumList.objects.get(pk=id)

    album_info = {
        'album': album.album_name,
        'publish_date': album.publish_date.strftime('%Y-%m-%d'),
        'album_state': album.album_status,
        'album_pic_url': album.album_pic_url.url,
    }
    audio_list = []

    for a in TAudioList.objects.filter(album_id=id):
        temp = {
            'audio_name': a.audio_name,
            'audio_url': a.audio_url.url,
            'audio_status': a.audio_status
        }
        audio_list.append(temp)

    album_info['list'] = audio_list

    return album_info


@method_decorator(csrf_exempt, name='dispatch')
class Regist(View):

    def get(self, request, *args, **kwargs):
        u_list = []
        for u in TUser.objects.all():
            temp = {
                'id': u.id,
                'realname': u.realname,
                'password': u.password,
                'location': u.location
            }
            u_list.append(temp)
        u_json = json.dumps(u_list)
        return HttpResponse(u_json)

    def post(self, request, *args, **kwargs):
        realname = request.POST.get('user')
        password = request.POST.get('pwd')

        try:
            with transaction.atomic():
                user = TUser.objects.create(realname=realname, password=password)
                msg = {
                    'realname': user.realname,
                    'password': user.password,
                    'id': user.id
                }
        except:
            msg = {
                "errno": "-200",
                "error_msg": "该手机号已经存在"
            }
        return HttpResponse(json.dumps(msg))

    def put(self, request, *args, **kwargs):
        put_dict = QueryDict(request.body)
        uid = put_dict.get('id')
        try:
            user = TUser.objects.get(pk=uid)
            gender = put_dict.get('gender')
            location = put_dict.get('location')
            nickname = put_dict.get('nickname')
            realname = put_dict.get('realname')
            sign = put_dict.get('sign')
            age = put_dict.get('age')
            password = put_dict.get('password')
            user.gender = gender
            user.location = location
            user.nickname = nickname
            user.realname = realname
            user.sign = sign
            user.age = age
            user.password = password
            user.save()
            
            msg = {
                'gender': gender,
                'location': location,
                'nickname': nickname,
                'realname': realname,
                'sign': sign,
                'age': age,
                'password': password,
            }

        except:
            msg = {
                "errno": "-200",
                "error_msg": "该手机号已经存在"

            }

        return HttpResponse(json.dumps(msg))

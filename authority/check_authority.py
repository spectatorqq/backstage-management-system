import re

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from chimingfazhou import settings


class Check(MiddlewareMixin):

    def process_request(self, request):
        """
        比对用户登录成功后存入session的url和请求url， 是否匹配
        匹配成功才可以访问
        :param request:
        :return:
        """
        white_list = [
            '/authority/login',
            '/authority/login_logic',
            '/admin/.*'
        ]

        current_url = request.path
        if current_url == '/':
            return redirect('/authority/login/')

        permission_list = request.session.get(settings.PERMISSION_URL)
        print(permission_list)
        for w in white_list:
            if re.match(w, current_url):
                return

        if not permission_list:
            return HttpResponse('请登录')

        if current_url not in permission_list:
            return HttpResponse('您没有相应权限')

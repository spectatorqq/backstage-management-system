from django.http import HttpResponse
from django.shortcuts import render
from django.core import cache
# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from chimingfazhou import settings
from utils.gen_code import gen_code
from utils.yunpian import YunPian, red
from mana.models import TCarousel


@cache_page(timeout=60*60, key_prefix='main')
def home(request):
    c = TCarousel.objects.filter(img_status=1)
    return render(request, 'main.html', {'c': c})


@cache_page(timeout=60*60, key_prefix='login')
def login(request):
    return render(request, 'login.html')


@csrf_exempt
def send_code(request):
    mobile = request.POST.get('mobile')
    yunpian = YunPian(settings.API_KEY)
    code = gen_code()
    res = yunpian.send_msg(mobile, code)
    if res == 'exist':
        return HttpResponse('大哥，验证码60秒内有效，看看手机吧')
    elif res == 'ok':
        return HttpResponse('ok')
    elif res == 'failed':
        return HttpResponse('发送失败')


@csrf_exempt
def login_logic(request):
    mobile = request.POST.get('mobile')
    code = request.POST.get('code')
    r_code = red.get(mobile)
    if r_code:
        if code == r_code.decode():
            return HttpResponse('ok')
    else:
        return HttpResponse('failed ')

from authority.models import Staff, Permission
from chimingfazhou import settings


def save_permission(s: Staff, request):
    # 获取用户的权限列表
    permission_list = s.role.filter(permission__isnull=False).values('permission__url',
                                                                     'permission__id',
                                                                     'permission__parent_id',
                                                                     'permission__title',
                                                                     'permission__is_menu',
                                                                     'permission__level',
                                                                     'permission__nickname').distinct()
    # 将权限url存入列表
    per_list = [item['permission__url'] for item in permission_list]
    # 将用户有权限的菜单列表存入session
    menu_list = []
    for url in permission_list:
        if url['permission__level'] == 1 and url['permission__is_menu']:
            submenu = []
            for p in permission_list:
                if p['permission__parent_id'] == url['permission__id']:
                    temp = {
                        'title': p['permission__title'],

                        'url': p['permission__url']
                    }
                    submenu.append(temp)

            menu_dict = {
                'title': url['permission__title'],
                'nickname': url['permission__nickname'],
                'content': submenu
            }
            # 找到一个一级菜单就将它和它的二级菜单放进列表中
            menu_list.append(menu_dict)
    request.session['name'] = s.name
    print(request.session['name'])
    request.session[settings.MENU_URL] = menu_list
    request.session[settings.PERMISSION_URL] = per_list
    # print(request.session[settings.MENU_URL])
    # print(request.session[settings.PERMISSION_URL])

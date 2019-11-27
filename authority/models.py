from django.db import models

# Create your models here.


class Permission(models.Model):

    title = models.CharField(max_length=255, verbose_name='权限名称', )
    nickname = models.CharField(max_length=255, verbose_name='id别称', blank=True, null=True,)
    url = models.CharField(max_length=255, verbose_name='请求路径', blank=True, null=True)
    level = models.IntegerField(verbose_name='请求等级')
    parent_id = models.IntegerField(verbose_name='上级id ')
    is_menu = models.BooleanField(verbose_name='是否是菜单', default='0')

    class Meta:
        db_table = 't_permission'

    def __str__(self):  # 重写__str__方法
        return self.title


class Role(models.Model):

    title = models.CharField(max_length=255, verbose_name="角色名称")
    permission = models.ManyToManyField(to='Permission', blank=True, verbose_name='角色对应权限')

    class Meta:
        db_table = 't_role'

    def __str__(self):  # 重写__str__方法
        return self.title


class Staff(models.Model):

    name = models.CharField(max_length=255, verbose_name='人员名称')
    password = models.CharField(verbose_name='密码', max_length=255)
    role = models.ManyToManyField(verbose_name='职员角色', to='Role', blank=True,)

    class Meta:
        db_table = 't_staff'

    def __str__(self):  # 重写__str__方法
        return self.name

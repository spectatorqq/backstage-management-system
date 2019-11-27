from django.contrib import admin

# Register your models here.
from authority.models import Role, Permission, Staff

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Staff)

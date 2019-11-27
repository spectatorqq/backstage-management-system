import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chimingfazhou.settings")
django.setup()
from django.test import TestCase
from authority.models import Role, Permission, Staff
# Create your tests here.

s1 = Staff.objects.get(pk=1)
print(s1.role.values('title'))
print(','.join([x['title'] for x in s1.role.values('title')]))
from django.apps import AppConfig
from django.contrib import admin
from authority.models import Role, Permission, Staff


class AuthorityConfig(AppConfig):
    name = 'authority'



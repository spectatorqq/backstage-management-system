# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAlbumList(models.Model):
    album_name = models.CharField(max_length=255, blank=True, null=True)
    album_info = models.TextField(blank=True, null=True)
    album_author = models.IntegerField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    album_status = models.CharField(max_length=255, blank=True, null=True)
    stars = models.CharField(max_length=255, blank=True, null=True)
    speaker_id = models.IntegerField(blank=True, null=True)
    episode_number = models.CharField(max_length=255, blank=True, null=True)
    content_brief = models.TextField(blank=True, null=True)
    album_pic_url = models.ImageField(upload_to='album', blank=True, null=True)

    class Meta:
        db_table = 't_album_list'


class TArticleList(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    cate = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    article_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_article_list'


class TAudioList(models.Model):
    audio_name = models.CharField(max_length=255, blank=True, null=True)
    album_id = models.IntegerField(blank=True, null=True)
    audio_url = models.FileField(upload_to='audio', blank=True, null=True)
    audio_time = models.CharField(max_length=255, blank=True, null=True)
    audio_size = models.CharField(max_length=255, blank=True, null=True)
    audio_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_audio_list'


class TCarousel(models.Model):
    img_name = models.CharField(max_length=255, blank=True, null=True)
    img_desc = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.ImageField(blank=True, null=True, upload_to='banner')
    img_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_carousel'


class TCounter(models.Model):
    counter_name = models.CharField(max_length=255, blank=True, null=True)
    cur_number = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    lesson_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_counter'


class TGuru(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    guru_status = models.CharField(max_length=255, blank=True, null=True)
    guru_pic_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_guru'


class TLesson(models.Model):
    lesson_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lesson'


class TManager(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_manager'


class TUser(models.Model):
    realname = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_status = models.CharField(max_length=255, blank=True, null=True)
    portrait_url = models.ImageField(blank=True, null=True, upload_to='user_portrait')
    location = models.CharField(max_length=255, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TArticlePic(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    pic = models.ImageField(upload_to='article_pic', blank=True, null=True)

    class Meta:
        db_table = 't_article_pic'

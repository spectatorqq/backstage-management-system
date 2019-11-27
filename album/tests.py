from django.test import TestCase
import requests
# Create your tests here.

download_url1 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(2142273838)
download_url2 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(1383927243)
download_url3 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(1399533630)
download_url4 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(29004400)
download_url5 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(27808044)
download_url6 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(65919)
download_url7 = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(167870)

headers = {
'referer': 'https://music.163.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}

res = requests.get(download_url1, headers=headers)
print(res.status_code)
with open('music/世间美好与你环环相扣.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url2, headers=headers)
print(res.status_code)
with open('music/这一生关于你的风景.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url3, headers=headers)
print(res.status_code)
with open('music/与火星的孩子对话.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url4, headers=headers)
print(res.status_code)
with open('music/烟火里的尘埃.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url5, headers=headers)
print(res.status_code)
with open('music/丑八怪.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url6, headers=headers)
print(res.status_code)
with open('music/K歌之王.mp3', 'wb') as w:
    w.write(res.content)
res = requests.get(download_url7, headers=headers)
print(res.status_code)
with open('music/如果当时.mp3', 'wb') as w:
    w.write(res.content)



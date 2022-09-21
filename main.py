from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()

start_date = "2021-2-14"  
city = "101281001"         
app_id = "wx98cc4c3242d935cc" 
app_secret = "7384de710f9c0ba63b89c27aa334193d" 
user_id = "oPjaC6pn0u-sJVAZGYopI-rgxXtc"        
template_id = "	5RE8DvgEVWTNQaha2SaXacfXvX-w4zScQ4RNxTkEGm82" 


def get_weather():
  # url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  url = "http://t.weather.sojson.com/api/weather/city/" + city
  res = requests.get(url).json()
  # weather = res['data']['list'][0]
  weather = res['data']
  return weather['quality'], weather['wendu']
  # return weather['quality'], math.floor(weather['wendu'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)

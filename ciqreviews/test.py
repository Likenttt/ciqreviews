
# -*- coding: UTF-8 -*-
import argparse
from connectiq import get_html_text_from_url, get_user_app_download_info, get_app_download_info, get_app_rating, analyse_local_reviews_data, get_single_page_review_json_using_bs4, analyse_remote_reviews_data, analyse_local_reviews_data, get_multi_page_review_json_using_bs4
import os
import urllib.parse


# clear my proxy temporarily
os.environ["http_proxy"] = ''
os.environ["https_proxy"] = ''
print(os.environ["http_proxy"])
print(os.environ["http_proxy"])

# # 下载json评论数据
# get_multi_page_review_json_using_bs4(
#     'https://apps.garmin.cn/en-US/apps/6c5b540e-32f3-40b3-9913-9ba196739fab')

# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_GRun中文版_62278_208.json'))
# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_Quatro 中文版_23194_1580.json'))
# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_JumpJump跳绳_42885_232.json'))

# analyse_remote_reviews_data(
#     'https://apps.garmin.cn/zh-CN/apps/dc6ceca8-6ec6-49f2-b711-4ebc0d347177')


# app_name_com, total_downloads, total_reviews, average_rating = get_app_download_info(
#     'dc6ceca8-6ec6-49f2-b711-4ebc0d347177', 'com')
# print(app_name_com, total_downloads, total_reviews, average_rating)

# Generate multi-badges
developer_name, total_download, app_dict = get_user_app_download_info(
    '876cfd5e-4e42-48ca-8869-cd7c59235573', 'all')

# developer_name, total_download, app_dict = get_user_app_download_info(
#     'cdc2c15c-3ac3-46c6-99ec-a9c0f4a135e0', 'all') #li2niu

print('{}: total downloads:{} downloads rank;{}'.format(
    developer_name, total_download, app_dict))

template = '''
![{}](https://img.shields.io/badge/dynamic/json?color=green&label={}%20Global%20Downloads&style=flat-square&query=downloads&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dall)
![{}](https://img.shields.io/badge/dynamic/json?color=green&label={}%20ROW%20Downloads&style=flat-square&query=downloads&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dcom)
![{}](https://img.shields.io/badge/dynamic/json?color=green&label={}%20China%20Downloads&style=flat-square&query=downloads&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dcn)
![{}](https://img.shields.io/badge/dynamic/json?color=blue&label={}%20ROW%20Rating&style=flat-square&query=ratings&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dcom)
![{}](https://img.shields.io/badge/dynamic/json?color=blue&label={}%20China%20Rating&style=flat-square&query=ratings&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dcn)
![{}](https://img.shields.io/badge/dynamic/json?color=orange&label={}%20Reviews&style=flat-square&query=reviews&url=https%3A%2F%2Fciqstats.li2niu.com%2Fapi%2Fstats%3Fappid%3D{}%26domain%3Dall)

'''

for appid, app in app_dict.items():
    if app['total_downloads'] <= 1000:
        continue
    urlencoded_app_name = urllib.parse.quote(
        app['app_name'])
    print(template.format(app['app_name'], urlencoded_app_name, appid, app['app_name'], urlencoded_app_name, appid, app['app_name'], urlencoded_app_name,
          appid, app['app_name'], urlencoded_app_name, appid, app['app_name'], urlencoded_app_name, appid, app['app_name'], urlencoded_app_name, appid))

# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 7:00 PM
# @Author  : Jihu Sun
# @FileName: logout.py
# @Software: PyCharm

import requests
import urllib3

urllib3.disable_warnings()


def logout(ip):
    """
    设备登陆注销
    :return: 注销结果
    """
    url = "https://{}:4343/v1/api/logout".format(ip)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    payload = {}

    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        status = response.json()['_global_result']['status']
        status_str = response.json()['_global_result']['status_str']

        if status == '0':
            uid_aruba = None
            print("logout {} | {}".format(ip, status_str))
        else:
            print("logout failed!")
    except requests.exceptions.ConnectionError as e:
        # print(e.args[0].reason)
        print("logout {} |".format(ip), str(e.args[0].reason).split(':')[2])

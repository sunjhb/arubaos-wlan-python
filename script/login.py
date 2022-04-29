# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 7:00 PM
# @Author  : Jihu Sun
# @FileName: logout.py
# @Software: PyCharm

import requests
import urllib3

urllib3.disable_warnings()


def login(ip, username, password):
    """
    设备登陆
    :return: uidaruba，即cookie
    """
    url = "https://{}:4343/v1/api/login".format(ip)
    payload = {
        'username': username,
        'password': password,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        status = response.json()['_global_result']['status']
        status_str = response.json()['_global_result']['status_str']

        if status == '1':
            print("login {} | {}".format(ip, status_str))
            return None

        elif status == '0':
            uid_aruba = response.json()['_global_result']['UIDARUBA']
            print("login {} | {} | UIDARUBA: {}".format(ip, status_str, uid_aruba))
            return uid_aruba

    except requests.exceptions.ConnectionError as e:
        print("login {} |".format(ip), str(e.args[0].reason).split(':')[2])
        return None

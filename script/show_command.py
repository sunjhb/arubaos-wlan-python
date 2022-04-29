# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 7:07 PM
# @Author  : Jihu Sun
# @FileName: show_command.py
# @Software: PyCharm

import requests
import urllib3

urllib3.disable_warnings()


def show_command(ip, uid_aruba, command):
    """
    :param ip:         设备ip地址
    :param uid_aruba:  登陆cookie
    :param command:    show 命令
    :return:           show 结果
    """
    url = "https://{ip}:4343/v1/configuration/showcommand?command={command}&UIDARUBA={uid}".format(
        ip=ip,
        command=command,
        uid=uid_aruba,
    )

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'SESSION={}'.format(uid_aruba),
    }

    try:
        response = requests.request("GET", url, headers=headers, verify=False)
        return response

    except requests.exceptions.ConnectionError as e:
        print(e.args[0].reason)

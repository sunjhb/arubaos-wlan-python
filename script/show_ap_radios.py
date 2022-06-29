# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 9:02 AM
# @Author  : Jihu Sun
# @FileName: show_ap_radios.py
# @Software: PyCharm
from script.show_command import show_command


def show_ap_radios(ip, uid_aruba):
    """
    :param ip:
    :param uid_aruba:
    :return:
    (host) #show ap radio-summary
    APs Radios information
    ----------------------
    Name         Group    AP Type  IP Address    Band  Mode         EIRP/MaxEIRP  NF/U/I     TD           TM           TC
    ----         -----    -------  ----------    ----  ----         ------------  ------     --           --           --
    AP203RP-new  default  203RP    192.168.1.12  2.4   AP:HT:1      15.8/23.0     -93/24/21  0/0/0/0/0/0  0/0/0/0/0/0  0/0/0/0/0/0
    AP203RP-new  default  203RP    192.168.1.12  5     AP:VHT:149E  15.7/22.5     -97/5/4    0/0/0/0/0/0  0/0/0/0/0/0  0/0/0/0/0/0

    NF: Noise Floor(dBm); U: Utilization(%); I: Interference(%)
    Mode: HT or VHT mode followed by Key Word "SCH" indicates that single chain mode is enabled on this radio
    TD/TM/TC(*/*/*/*/*/*): "*" is the time used by Data/Mgmt/Ctrl Frames(%) in a 10 seconds time slot in the past 1 minute
    AP followed by "^" indicates that spectrum monitoring is enabled on the radio in AP mode
    """

    cmd = "show ap radio-summary"
    resp = show_command(ip, uid_aruba, command=cmd)
    return resp

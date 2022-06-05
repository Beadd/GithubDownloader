
from itertools import count
import os
import json
import requests


mode = '0'
string = "\/:*?\">|"
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
proxies = {"http": None, "https": None}

def Start():
    global mode
    print("下载用户所有的Star仓库\t1")
    print("下载用户的所有仓库    \t2")
    mode = input("请选择:")
    if mode == '1':
        print("下载所有Star仓库")
        return 1
    if mode == '2':
        print("下载所有仓库")
        return 2
    else:
        print("选择数字有误")
        return 0


def UsersStar():
    counter = 1
    username = input("请输入用户名:")
    source = "https://api.github.com/users/" + str(username) + "/starred"
    response = requests.get(source, headers=header, proxies=proxies)
    data = json.loads(response.text)
    if 'message' in data:
        return 0
    for i in string:
        if i in username:
            username = "NameFalseNo."
    if (os.path.exists(username+"-stars") == False):
        os.system("mkdir "+username+"-stars")
    for data in data:
        print(str(counter) + ' ' + data['name'] + "-" + data['owner']['login'])
        url = "https://github.com/" + data[
            'full_name'] + "/archive/refs/heads/" + data[
                'default_branch'] + ".zip"
        req = requests.get(url, headers=header, proxies=proxies)
        name_url = username+"-stars"+"/"+data['name']+"-"+data['owner']['login']+".zip"
        with open(name_url, "wb") as code:
            code.write(req.content)
        counter += 1


def UsersRepos():
    counter = 1
    username = input("请输入用户名:")
    source = "https://api.github.com/users/"+str(username)+"/repos"
    response = requests.get(source, headers=header, proxies=proxies)
    data = json.loads(response.text)
    if 'message' in data:
        return 0
    for i in string:
        if i in username:
            username = "NameFalseNo."
    if (os.path.exists(username+"-repos") == False):
        os.system("mkdir "+username+"-repos")
    for data in data:
        print(str(counter) + ' ' + data['name'] + "-" + data['owner']['login'])
        url = "https://github.com/" + data[
            'full_name'] + "/archive/refs/heads/" + data[
                'default_branch'] + ".zip"
        req = requests.get(url, headers=header, proxies=proxies)
        name_url = username + "-repos" + "/" + data['name'] + "-" + data['owner'][
            'login'] + ".zip"
        with open(name_url, "wb") as code:
            code.write(req.content)
        counter += 1




os.system("cls")
print("C Beadd")
print("感谢使用!")
#print("下载文件自动放在当前目录StarB中")
# while 1:
#     if mode == 0:
#         start = Start()
#         if start == 1:
#             os.system("cls")
#             print("开始下载用户Star")
#             if UsersStar() == 0:
#                 print("用户不存在或者并无Star!")
#                 os.system("pause")
#         if start == 2:
#             os.system("cls")
#             print("开始下载用户Reop")
#     if mode == 1:
#         os.system("cls")
#         print("开始下载用户Star")
#         if UsersStar() == 0:
#             print("用户不存在或者并无Star!")
#             os.system("pause")
#     if mode == 2:
#         os.system("cls")
#         print("开始下载用户Reop")
#     else:
#         print("请输入正确数字")
#         os.system("pause")
while 1:
    if mode == '0':
        start = Start()
        if start == 0:
            mode = '0'
            print("请输入正确数字")
            continue
    if mode == '1':
        if UsersStar() == 0:
            print("用户不存在或者并无Star!")
            os.system("pause")
            continue
        else:print("下载完成!")
    if mode == '2':
        if UsersRepos() == '0':
            print("用户不存在或者并无仓库!")
            os.system("pause")
        else:print("下载完成")
    else:continue

import os
import json
import requests

header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
proxies = {"http": None, "https": None}


def start():
    counter = 1
    username = input("请输入用户名:")
    source = "https://api.github.com/users/" + str(username) + "/starred"
    response = requests.get(source, headers=header, proxies=proxies)
    data = json.loads(response.text)
    if 'message' in data:
        return 0
    os.system("mkdir StarB")
    for data in data:
        print(str(counter) + ' ' + data['name'] + "-" + data['owner']['login'])
        url = "https://github.com/" + data[
            'full_name'] + "/archive/refs/heads/" + data[
                'default_branch'] + ".zip"
        req = requests.get(url, headers=header, proxies=proxies)
        name_url = "StarB/" + data['name'] + "-" + data['owner'][
            'login'] + ".zip"
        with open(name_url, "wb") as code:
            code.write(req.content)
        counter += 1


os.system("cls")
print("C Beadd")
print("下载文件自动放在当前目录StarB中")
while 1:
    if start() == 0:
        print("用户不存在或者并无Star!")
        os.system("pause")
    else:
        print("下载完成!感谢使用")
        os.system("pause")
        break

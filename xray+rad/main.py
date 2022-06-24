import argparse
import os
import threading
import time

t=time.localtime()
mz=str(t.tm_hour) +"." +str(t.tm_min)+"."+str(t.tm_sec)
def xray():
    os.system(f"Xray\\xray_windows_amd64.exe webscan --listen 127.0.0.1:7777 --html-output {mz}.html")
def rad():
    os.system(f'Rad\\rad_windows_amd64 -t {dlj} --http-proxy 127.0.0.1:7777')


if __name__ =="__main__":
    try:
        parser = argparse.ArgumentParser(description='命令行中传入一个数字')
        parser.add_argument('-u', type=str, help='传入链接 -u http://baidu.com/')
        args = parser.parse_args()
        t1 = threading.Thread(target=xray)
        t2 = threading.Thread(target=rad)
        if args.u!=None:
            dlj=args.u
            t1.start()
            t2.start()
    except:
        print("乖点，听话，按我的提示打命令")

        
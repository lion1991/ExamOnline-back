import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json

URL = "https://oapi.dingtalk.com/robot/send?access_token=092a743a46c1a592f11b38574630cc2443f44da117601ce6a4611441c67d8c87"

 # 钉钉机器人文档说明
 # https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

def get_timestamp_sign():
    timestamp = str(round(time.time() * 1000))
    #secret = "SEC6886eee211cce899b269749c312bd38a220ef24b6f82b855c9040a13e6****" # SEC开头的
    secret = "SECcba866bbef13af3cb38abe77a1e235c0d3d1f214e4bc6b73281eecab4dc958f0"
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print("timestamp: ",timestamp)
    print("sign:",sign)
    return (timestamp, sign)


def get_signed_url():
    timestamp, sign = get_timestamp_sign()
    webhook = URL + "&timestamp="+timestamp+"&sign="+sign
    return webhook

def get_webhook(mode):

    if mode == 0: # only 敏感字
       webhook = URL
    elif mode == 1 or  mode ==2 : # 敏感字和加签 或 # 敏感字+加签+ip
        # 加签： https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        webhook = get_signed_url()
    else:
        webhook = ""
        print("error! mode:   ",mode,"  webhook :  ",webhook)
    return webhook

def get_message(content,is_send_all):
    # 和类型相对应，具体可以看文档 ：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
    # 可以设置某个人的手机号，指定对象发送
    message = {
        "msgtype": "text", # 有text, "markdown"、link、整体跳转ActionCard 、独立跳转ActionCard、FeedCard类型等
        "text": {
            "content": content # 消息内容
        },
        "at": {
            "atMobiles": [
                 "13945020223",
             ],
            "isAtAll": is_send_all # 是否是发送群中全体成员
        }
    }
    print(message)
    return message

def send_ding_message(content,is_send_all):
    # 请求的URL，WebHook地址
    webhook = get_webhook(1) # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
    print("webhook: ",webhook)
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 构建请求数据
    message = get_message(content,is_send_all)
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)

if __name__ == "__main__":
    content     = "test,机器人测试,hello！"
    is_send_all = True
    send_ding_message(content,is_send_all)
#!/user/bin/env python
# coding:utf-8
import requests
import json
import sys, locale
import time
from collections import OrderedDict
import hashlib
import hmac
import base64
import random
import urllib.parse
import re

def valiOpenApiTest():
    baseUrl = "http://vali-inner-api.shd.vali.com.cn"
 
 api = "/vali/business/api/v1/clusters/79f43a0e540dfc8d5234121123237258bc3af/namespaces/vali-pae/pods?searchName&pageNum=1&pageSize=10"
 method = "get"
 
 null = None
 param = {
    }
    body_form_text = {
    }
    body_form_file = {
    }
    body_raw = {}

 sk = "c0885357-5c5f-4a45-8965-23d"
 alg = "SHA256"
 # 定义cookie，请求头中使用，决定指向环境
 cookieValue = "vali-test=blue"
 # 获取当前时间戳并转java的长整型
 # timestamp = str(int(time.time() * 1000)) timestamp = str(int(time.time()))
    print ("----timestamp----")
    print (timestamp)
    # 获取6位随机数
 index = 6
 count = 0
 num = ""
 while index > count:
        num = num + str(random.randrange(0, 10))
        count += 1
 print ("----random----")
    print (num)
    # 拼接apiurl
 apiurl = ""
 if "{" in api and len(param) != 0:
        apiurl = api.format(**param)
    else:
        apiurl = api
    print ("----apiurl----")
    print (apiurl)
    # param的排序拼接
 if "{" not in api and len(param) != 0:
        paramKeyList = sorted(param.keys())
        print ("----paramKeyList----")
        print (paramKeyList)
        paramOrder = ""
 for item in paramKeyList:
            paramOrder = paramOrder + item + "=" + str(param[item]) + ";"
 else:
        paramOrder = ""
 print ("----paramOrder----")
    print (paramOrder)
    # 计算签名时body的处理
 bodyDict = {}
    # if len(body_raw) != 0:
 #     bodyDict = body_raw # elif len(body_form_text) != 0: #     body_form_text_keyList = sorted(body_form_text.keys()) #     body_form_text_order = "" #     for item in body_form_text_keyList: #         body_form_text_order = body_form_text_order + item + "=" + str(body_form_text[item]) + ";" # else: #     bodyDict = {} print ("----bodyDict----")
    print (bodyDict)
    if len(bodyDict) == 0:
        bodyJson = ""
 else:
        bodyJson = json.dumps(bodyDict, separators=(",", ":"), ensure_ascii=False)
    print ("----bodyJson----")
    print (bodyJson)
    # 拼接签名参数并转小写
 queryStr = ak + "&" + apiurl + "&" + paramOrder + "&" + bodyJson + "&" + timestamp + "&" + num
    lowerQueryStr = queryStr.lower()
    print ("----lowerQueryStr----")
    print (lowerQueryStr)
    # 获取签名
 signature1 = hmac.new(sk.encode('utf-8'), lowerQueryStr.encode('utf-8'), digestmod=hashlib.sha256).digest()
    print ("----sha256----")
    print (signature1)
    # signature0 = str(signature1,encoding='utf-8')
 signature2 = base64.b64encode(signature1)
    print ("----base64----")
    print (signature2)
    signature = urllib.parse.quote(signature2, safe='', encoding=None, errors=None)
    print ("----signature----")
    print (signature)
    # 请求头
 headers = {"apiKey": ak, "signature": signature, "timestamp": timestamp, "random": num, "alg": alg,
 "cookie": cookieValue}
    # 拼接请求url
 if "{" in api and len(param) != 0:
        url = baseUrl + apiurl
    elif len(param) != 0:
        paramStr = ""
 for key in param.keys():
            paramStr = key + "=" + str(param[key]) + "&" + paramStr
        url = baseUrl + apiurl + "?" + paramStr[:-1]
    else:
        url = baseUrl + apiurl
    print ("----url----")
    print (url)
    # 发送请求时body的处理
 headers["Content-Type"] = "application/json"
 if len(body_raw) != 0:
        bodyRequest = json.dumps(body_raw, separators=(",", ":"), ensure_ascii=False)
    elif len(body_form_text) != 0 or len(body_form_file) != 0:
        bodyRequest = body_form_text
    else:
        bodyRequest = ""
 print ("----bodyRequest----")
    print (bodyRequest)
    # 发送请求
 if method.lower() == "get":
        response = requests.get(url, data=bodyRequest, headers=headers, verify=False)
    elif method.lower() == "put" and len(body_form_file) == 0:
        response = requests.put(url, data=bodyRequest, headers=headers, verify=False)
    elif method.lower() == "put" and len(body_form_file) != 0:
        response = requests.put(url, files=body_form_file, data=bodyRequest, headers=headers, verify=False)
    elif method.lower() == "post" and len(body_form_file) == 0:
        response = requests.post(url, data=bodyRequest, headers=headers, verify=False)
    elif method.lower() == "post" and len(body_form_file) != 0:
        response = requests.post(url, files=body_form_file, data=bodyRequest, headers=headers, verify=False)
    elif method.lower() == "delete":
        response = requests.delete(url, data=bodyRequest, headers=headers, verify=False)
    print ("----response----")
    print (response)
    print ("----response text----")
    print (response.text)
if __name__ == '__main__':
    valiOpenApiTest()
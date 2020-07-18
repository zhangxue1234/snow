"""
# @Time : 2020/7/10 0010 17:27
# @Author : zhangxue
"""
import requests
import json
url = "http://bptest.herbalifeonline.cn/apitest/test/member/api/member/getCustomerAssociation"
headers = {"Content-Type":"application/json"}
data = {"openId": "o63fc4lwbqQjAwLNJdrJJEoqHLRc"}
re = requests.post(url,data=json.dumps(data),headers=headers)
print(type(re))
b = re.json()
print(type(b))
# result =
# print(result)
print(b.get("accessToken"))

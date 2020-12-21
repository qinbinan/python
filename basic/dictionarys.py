# -*- coding: utf-8 -*-
# 字典
# 定义
empinfo = {
    'empno':7788,
    'ename':'smith',
    'job':'clerk',
    'sal':800,
    'cost':['桑拿', '采耳', '搓澡']
}

# 访问  通过key找value
print(empinfo.get('cost','caichang'))

print(empinfo.get('ename'))
print(empinfo['ename'])

print(empinfo.keys())
print(type(empinfo.keys()))


result = {
    "resultcode": "200",
    "reason": "Return Successd!",
    "result": {
        "province": "重庆",
        "city": "重庆",
        "areacode": "023",
        "zip": "404100",
        "company": "联通",
        "card": "18602355173"
    },
    "error_code": 0
}

print(result['resultcode'])
print(result['result']['province'])

if result['resultcode']=="200":
    print(list(result['result'].values()))

